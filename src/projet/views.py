from django.shortcuts import render

from projet.services.calendar import WorkingDaysService


def index(requests):
    return render(requests, "projet/index.html")

def working_days_view(request, year):
    # Assuming you want to get the working days for the given 'year'
    working_days = WorkingDaysService().get_working_days(year)

    # You can use 'working_days' in your template or perform other operations

    context = {
        'year': year,
        'working_days': working_days,
    }

    return render(request, 'projet/working_days_template.html', context)