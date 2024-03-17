
// function getSpeciAllList()
// {
//     const div_regioni = document.getElementById('regioni_all_list');
//     const button_for_regioni = document.getElementById('button_regioni');
//     const div_cut_regioni = document.getElementById('regioni_cut_list');

//     if (button_for_regioni.textContent == 'Показать все')
//     {
//         div_cut_regioni.hidden = true;
//         div_regioni.hidden = false;
//         button_for_regioni.textContent = 'Свернуть';
//     }
//     else {
//         div_cut_regioni.hidden = false;
//         div_regioni.hidden = true;
//         button_for_regioni.textContent = 'Показать все';
//     }
// }

// let regioni = [];

function addSpec(region)
{
    label = document.getElementById('vibrannie_regioni');
    label.hidden = false;
    if (!specs.includes(region))
    {
        specs.push(region)
    }
    else {
        const index = regioni.indexOf(region);
        specs.splice(index, 1);
        if (specs.length == 0) label.hidden = true;
    }
    let string = specs.toString();
    string = string.replace(',', ', ');
    label.textContent = string;
}
let specs = []
// let specs = document.getElementById('checked_spec')? document.getElementById('checked_spec').split(','): [];

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
    
    _start();
}

let services = [];

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

    _start();
}


async function _start()
{
    await new Promise(r => setTimeout(r, 1));
    console.log('start');

    let services_value = document.getElementById('checked_services').value;
    if (services_value != '')
        services = services_value.split(',');

    let specs_value = document.getElementById('checked_spec').value;
    if (specs_value != '')
        specs = specs_value.split(',');
    
    console.log(specs)
    console.log(services)

    for (let i = 0; i < services.length; i++)
    {
        document.getElementById(`service_${services[i]}`).checked = true;
    }

    for (let i = 0; i < specs.length; i++)
    {
        document.getElementById(`spec_${specs[i]}`).checked = true;
    }
}
_start();