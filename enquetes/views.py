from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Pergunta, Escolha

# views da aplicação enquetes




def index(request):
    dados = ''
    contexto = {
        "perguntas": {}
    }
    try:
        contexto['perguntas'] = Pergunta.objects.order_by( "texto" )
    except:
        print(f"LOG enquetes/ consulta falhou")
    return render( request, "enquetes/index.html", contexto )




def sobre(request):
    return HttpResponse( '<p> gerencie enquetes </p><a href="javascript:history.back()"> inicio </a>' )




def criarEnquete(request):
    return render( request, "enquetes/criarEnquete.html", {} )




def criarEnquetePost( request ):
    try:
        Texto = request.POST["texto"]

        # campoSGBD=Info
        novaEnquete = Pergunta( texto=Texto, date=timezone.now() )
        novaEnquete.save()
    except:
        return render( request, "enquetes/erro.html" )

    return HttpResponseRedirect( reverse( "enquetes:index" ) )





# http.param: pergunta_id
def visualizarEnquete(request, pergunta_id):
    consulta = ''
    opcoes = ''
    contexto = { }
    try:
        consulta =  Pergunta.objects.get( id=pergunta_id )
        opcoes = Escolha.objects.filter( pergunta=( Pergunta.objects.get(id= pergunta_id ) ) )
        contexto = {
            "pergunta_id": pergunta_id,
            "consulta": consulta,
            "opcoes": opcoes
        }
    except BaseException as e:
        print(f"FALHA: {e} ")
        return render( request, "enquetes/erro.html" )

    return render( request, "enquetes/visualizarEnquete.html", contexto )




def editarEnquetePatch(request, pergunta_id):
    try:
        alvo = Pergunta.objects.get(id=pergunta_id)
        alvo.texto = request.POST["texto"]
        alvo.save()
    except:
        return render( request, "enquetes/erro.html" )

    return HttpResponseRedirect( reverse( "enquetes:index" ) )




def deletarEnquete(request, pergunta_id):
    try:
        alvo = Pergunta.objects.get(id=pergunta_id)
        alvo.delete()
    except:
        return render( request, "enquetes/erro.html" )

    return HttpResponseRedirect( reverse( "enquetes:index" ) )




def visualizarEnquetes(request):
    pass

