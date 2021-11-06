
from django.shortcuts import render
from . models import Place , Team
# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, "index.html",{'result':obj,'result2':obj2})
