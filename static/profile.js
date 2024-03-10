function add_phone_panel(f)
{
    if (!f)
    {
        document.getElementById('add_phone_panel').hidden=false;
        document.getElementById('add_panel_knopka').setAttribute('onclick','add_phone_panel(1)');
        document.getElementById('add_panel_knopka').value='Скрыть';
    }
    else
    {
        document.getElementById('add_phone_panel').hidden=true;
        document.getElementById('add_panel_knopka').setAttribute('onclick','add_phone_panel(0)');
        document.getElementById('add_panel_knopka').value='Добавить';
    }
}

function add_service_panel(f)
{
    if (!f)
    {
        document.getElementById('add_service_panel').hidden=false;
        document.getElementById('add_panel_knopka_service').setAttribute('onclick','add_service_panel(1)');
        document.getElementById('add_panel_knopka_service').value='Скрыть';
    }
    else
    {
        document.getElementById('add_service_panel').hidden=true;
        document.getElementById('add_panel_knopka_service').setAttribute('onclick','add_service_panel(0)');
        document.getElementById('add_panel_knopka_service').value='Добавить';
    }
}

function add_button_rank(f)
{   
    if (!f)
    {
        document.getElementById('button_rank').hidden = false;
    }
}

function select_service()
{
    // spec_form, select
    // console.log("adASdqwd");
    document.getElementById("service_input").value = document.getElementById("select").value;
    console.log(document.getElementById("service_input").value)
}