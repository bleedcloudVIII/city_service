
function getRegioniAllList()
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

function addRegion(region)
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