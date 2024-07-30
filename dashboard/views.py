from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patrimonio.models import Item
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Sum


@login_required(login_url='login-page')
def dashboardpage(request):
    return render(request, "app/dashboard.html")


@login_required(login_url='login-page')
def retorna_total_gasto(request):
    total = Item.objects.all().aggregate(Sum('valorcompra'))['valorcompra__sum']
    return JsonResponse({'total': total})


@login_required(login_url='login-page')
def relatorio_gasto(request):
    x = Item.objects.all()

    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    datacompra = []
    labels = []
    const = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year

    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1

        y = sum([i.valorcompra for i in x if i.datacompra.month == mes and i.datacompra.year == ano])
        labels.append(meses[mes - 1])
        datacompra.append(y)
        const += 1

    data_json = {'datacompra': datacompra[::-1], 'labels': labels[::-1]}

    return JsonResponse(data_json)


@login_required(login_url='login-page')
def relatorio_marcas(request):
    x = Item.objects.all()

    label = []
    datacompra = []
    for x in i:
        valorcompra = Item.objects.filter(marca=x).aggregate(Sum('valorcompra'))
        if not valorcompra['valorcompra__sum']:
            valorcompra['valorcompra__sum'] = 0
        label.append(x.marca)
        datacompra.append(valorcompra['valorcompra__sum'])
    z = list(zip(label, datacompra))
    z.sort(key=lambda z: z[1], reverse=True)
    z = list(zip(*z))

    return JsonResponse({'labels': z[0][:3], 'datacompra': z[1][:3]})

