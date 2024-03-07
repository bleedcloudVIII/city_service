# from django.shortcuts import render, HttpResponseRedirect
# from django.contrib import auth
# from django.urls import reverse

# from companies.models import Company
# from users.models import User
# from django.contrib.auth.hashers import make_password, check_password

# from companies.forms import CompanyLoginForm, CompanyRegistrationForm

# # Ремонт
# # Пошив
# # Техническое обслуживание
# # Прачечная                           
# # Фотоателье
# # Баня
# # Парикмахерская
# # Ритуальные услуги

# def index(request):
#     # Пока не выбраны услуги и т.д.
#     # То берутся первые 10 компаний  
#     context = {
#         # 'companies': Company.objects.all(),
#         # 'companies': Company.objects.all(),
#         'spezs': [
#             {
#                 'name': 'Ремонт',
#             },
#             {
#                 'name': 'Пошив',
#             },
#             {
#                 'name': 'Техническое обслуживание',
#             },
#             {
#                 'name': 'Прачечная',
#             },
#             {
#                 'name': 'Фотоателье',
#             },
#             {
#                 'name': 'Баня',
#             },
#             {
#                 'name': 'Парикмахерчкая',
#             },
#             {
#                 'name': 'Ритуальные услуги',
#             },
#         ],
#         'services': [
#             {
#                 'name': 'Ремонт часов',
#             },
#             {
#                 'name': 'Ремонт мебели',
#             },
#         ],
#     }

#     return render(request, 'company_index.html', context)

# def registration(request):
# 		#     from django.contrib.auth.hashers import (
# 		#     check_password,
# 		#     is_password_usable,
# 		#     make_password,
# 		# )
#         # def set_password(self, raw_password):
#         # self.password = make_password(raw_password)
#         # self._password = raw_password
# 	# if request.method == 'POST':
# 	# 	user = User.objects.create(
# 	# 		first_name='yurii',
#    	# 		last_name='karas',
# 	# 		username='bleedcloud3',			
# 	# 	)
# 	# 	user.set_password('qweqe')
# 	# 	user.save()
# 	# 	user = User.objects.create(
# 	# 		first_name='yurii',
#    	# 		last_name='karas',
# 	# 		username='bleedcloud4',			
# 	# 		password='dwqweafwe'
# 	# 	)
# 	# 	user.save()
#     if request.method == 'POST':
#         print('REGISTRATION COMPANY')
#         print(request.POST)
#         form = CompanyRegistrationForm(data=request.POST)
#         if form.is_valid():
#             if request.POST['password1'] == request.POST['password2']:
#                 company = Company.objects.create(
#     				name=request.POST['name'],
# 				    login=request.POST['login'],
# 				    password=make_password(request.POST['password1'])
# 			    )
#                 return HttpResponseRedirect(reverse('company_login'))
#     else:
#         form = CompanyRegistrationForm()
#     context = {'form': form}
#     return render(request, 'company_registration.html', context)

# def authenticate(login=None, password=None, **kwargs):
#     try:
#         company = Company.objects.get(login=login)
#         if check_password(password, company.password):
#             return company
#         return None
#     except Company.DoesNotExist:
#         return None
            
# def logout(request):
#     print(request)
#     print(request.user)
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('company_index'))

# def login(request):
#     if request.method == 'POST':
#         print("LOGIN COMPANY")
#         print(request.POST)
#         form = CompanyLoginForm(data=request.POST)
#         print(form.errors.as_json)
#         if form.is_valid():
#             print('ASDQWDQWD')
#             login = request.POST['login']
#             password = request.POST['password']
#             company = authenticate(login, password)
#             print(company)
#             if company:
#                 print('wqdqqwd')
#                 # auth.login(request, company)
#                 print('adwd')
#                 return HttpResponseRedirect(reverse('company_index'))
#             else:
#               pass
#     else:
#         form = CompanyLoginForm()
#     context = {
# 		'form': form
# 	}
#     return render(request, 'company_login.html', context)


# def profile(request):
#    	return render(request, 'company_profile.html')