from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth



from users.forms import UserRegistrationForm, UserLoginForm
from users.models import User
    # path('cityserivce/users/registration/'),
    # path('cityserivce/users/login/'),
    # path('cityserivce/users/profile/'),
    
def registration(request):
    # 	form = CompanyRegistrationForm(data=request.POST)
	# if form.is_valid():
	# 	if request.POST['password1'] == request.POST['password2']:
	# 		company = Company.objects.create(
	# 			name=request.POST['name'],
	# 			login=request.POST['login'],
	# 			password=make_password(request.POST['password1'])
	# 		)
	# 		# company.save()
	# 		return HttpResponseRedirect(reverse('company_login'))
	# else:
	# 	form = CompanyRegistrationForm()
	# context = {'form': form}
	# return render(request, 'company_registration.html', context)
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        print(form.errors.as_json)
        if form.is_valid():
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    password=password1
                )
                return HttpResponseRedirect(reverse('user_login'))
            else:
                pass
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)

def login(request):
    #     if request.method == 'POST':
    #     form = CompanyLoginForm(data=request.POST)
    #     print(form.errors.as_json)
    #     if form.is_valid():
    #         print('ASDQWDQWD')
    #         login = request.POST['login']
    #         password = request.POST['password']
    #         company = authenticate(login, password)
    #         print(company)
    #         if company:
    #             print('wqdqqwd')
    #             # auth.login(request, company)
    #             print('adwd')
    #             return HttpResponseRedirect(reverse('company_index'))
    #         else:
    #           pass
    # else:
    #     form = CompanyLoginForm()
    # context = {
	# 	'form': form
	# }
    # return render(request, 'company_login.html', context)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username, password)
            if user:
                auth.login()
                return HttpResponseRedirect(reverse('company_index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def profile(request):
    return render(request, 'profile.html')