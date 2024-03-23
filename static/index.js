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

function pdf()
{
    const data = document.currentScript.dataset;
    console.log(data);
    // const username = data.username;
    // const data = JSON.parse(
    //     document.currentScript.nextElementSibling.textContent
    // );
    // var companies = JSON.parse('{{companies|escapejs}}');
    // console.log("DWWDSQQD");
    // const data = document.currentScript;
    // const username = data.username;
    // console.log(username);
    console.log(data);
    // console.log(companies)
}