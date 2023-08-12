from django.shortcuts import render
from celery.result import AsyncResult
from .tasks import add
# Create your views here.
def Home(request):
    context = {'mensaje': "Luis, Rodrigo, Hector"}
    
    return render(request,'test/test.html', context)

def celery_test(request):
    resultado = add.delay(5,6)

    #resultado = AsyncResult(resultado.id)
    resultado = resultado.get()
    resultado = str(resultado)
    context = {'resultado': resultado}

    return render(request,'test/celery.html', context)