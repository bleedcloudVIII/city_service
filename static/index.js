
function getSpeciAllList()
{
    const div_regioni = document.getElementById('regioni_all_list');
    const button_for_regioni = document.getElementById('button_regioni');
    const div_cut_regioni = document.getElementById('regioni_cut_list');

    if (button_for_regioni.textContent == 'Показать все')
    {
        div_cut_regioni.hidden = true;
        div_regioni.hidden = false;
        button_for_regioni.textContent = 'Свернуть';
    }
    else {
        div_cut_regioni.hidden = false;
        div_regioni.hidden = true;
        button_for_regioni.textContent = 'Показать все';
    }
}

let regioni = [];

function addSpec(region)
{
    label = document.getElementById('vibrannie_regioni');
    label.hidden = false;
    if (!regioni.includes(region))
    {
        regioni.push(region)
    }
    else {
        const index = regioni.indexOf(region);
        regioni.splice(index, 1);
        if (regioni.length == 0) label.hidden = true;
    }
    let string = regioni.toString();
    string = string.replace(',', ', ');
    label.textContent = string;
}

let specs = document.getElementById('checked_spec')? document.getElementById('checked_spec').split(','): [];

function spec(spec)
{
    // checked_spec
    values = document.getElementById('checked_spec');
    if (!specs.includes(spec))
    {
        specs.push(spec);
    }
    else
    {
        const index = specs.indexOf(spec);
        specs.splice(index, 1);
    }
    let string = specs.toString();
    values.value = string;
    // console.log(spec);
    console.log(values.value);
}


let services = document.getElementById('checked_services') ? document.getElementById('checked_services').split(','): [];

function q()
{
    console.log(specs)
    console.log(services)
}
function service(s)
{
    // checked_spec
    console.log(services)
    values = document.getElementById('checked_services');
    if (!services.includes(s))
    {
        services.push(s);
    }
    else
    {
        const index = services.indexOf(s);
        services.splice(index, 1);
    }
    let string = services.toString();
    values.value = string;
    // console.log(spec);
    console.log(values.value)
}