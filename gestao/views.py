from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from patrimonio.models import Item
from usuario.models import Setor


@login_required(login_url='login-page')
def localizar(request, id_setor):
    setor = get_object_or_404(Setor, id_setor=id_setor)
    itens = Item.objects.filter(setor_id_setor=setor)
    context = {
        'setor': setor,
        'itens': itens
    }
    return render(request, "app/localizacao.html", context=context)
