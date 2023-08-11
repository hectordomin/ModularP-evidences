from django.shortcuts import render
#from tasks import add
# Create your views here.
def Home(request):
    context = {'mensaje': "Luis, Rodrigo, Hector"}
    
    return render(request,'test/test.html', context)
