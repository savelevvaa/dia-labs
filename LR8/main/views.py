from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Phenomenon
from .models import Description

def index(request):
    phen_list = Phenomenon.objects.all()
    description = []
    for i in phen_list:
        description.append(get_object_or_404(Description, pk=i.id))
    context = {'title': 'Природные явления','phen_list': phen_list, 'disc':description}
    return render(request, 'main/index.html', context)


def details(request, phen_id):
    phen_list = Phenomenon.objects.all()
    for i in phen_list:
        if i.id == phen_id:
            phen = i
    description = get_object_or_404(Description, pk=phen_id)
    return render(request, 'main/details.html', {'pnen': phen, 'description': description})
