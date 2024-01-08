from django.shortcuts import render
from app.forms  import *
# Create your views here.
def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}

    if request.method=="POST":
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            TFDO=Topic.objects.all()
            d={'topicform':TFDO}
            return render(request,'display_topic.html',d)
        
    return render (request,'insert_topic.html',d)




def insertWebpage(request):
    EWFO=webpageform ()
    d={'EWFO':EWFO}
    if request.method=="POST":
        WFDO=webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            WFDO=Webpage.objects.all()
            d={'webpageform':WFDO}
            return render(request,'display_webpage.html',d)
    return render (request,'insertWebpage.html',d)




def insertAccess (request):
    EAFO=Accessform()
    d={'EAFO':EAFO}
    if request.method=="POST":
        AFDO=Accessform(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            AFDO=Access.objects.all()
            d={'accessform':AFDO}
            return render(request,'display_access.html',d)
    return render (request,'insertAccess.html',d)


























