from django.http import Http404
from django.shortcuts import render
from .models import Product,Game,Client,Remot,Video,Play,Dvd
# Create your views here.
def index(request):
    products=Product.objects.all()
    games=Game.objects.all()
    client=Client.objects.all()
    context={
       "products":products,
        "games":games,
        "client":client,

    }

    return render(request,"index.html",context=context)

def contact(request):
    return render(request,"contact.html",context={})

def video(request):
    video = Video.objects.all()
    context = {
        "video":video
    }
    return render(request,"video.html",context=context)

def product(request):
    video=Video.objects.all()
    remot=Remot.objects.all()
    context = {
        "remot":remot,
        "video":video
    }
    return render(request,"product.html",context=context)

def remot(request):
    remot = Remot.objects.all()
    dvd = Dvd.objects.all()
    context={
        "remot":remot,
        "dvd":dvd
    }
    return render(request,"remot.html",context=context)

def about(request):
    play = Play.objects.all()
    context={
        "play":play
    }
    return render(request,"about.html",context=context)
def productdetailview(request,id):
    try:
        product = Product.objects.get(id=id)
        context = {
            "products": product
        }
    except product.DoesNotExist:
        raise Http404("No product found")
    return render(request,"product_detail.html",context=context)


def gamedetailview(request,id):
    try:
        games = Game.objects.get(id=id)
        context = {
            "games":games
        }
    except games.DoesNotExist:
        raise Http404("No game found")
    return render(request,"game_detail.html",context=context)


def remotdetailview(request,id):
    try:
        remot=Remot.objects.get(id=id)
        context = {
            "remot":remot
        }
    except remot.DoesNotExist:
        raise Http404("No remot found")
    return render(request,"remot_detail.html",context=context)

def videodetailview(request,id):
    try:
        video=Video.objects.get(id=id)
        context = {
            "video":video
        }
    except video.DoesNotExist:
        raise Http404("No video found")
    return render(request,"video_detail.html",context=context)

def clientdetailview(request,id):
    try:
        client=Client.objects.get(id=id)
        context = {
            "client":client
        }
    except client.DoesNotExist:
        raise Http404("No client found")
    return render(request,"client_detail.html",context=context)


def playdetailview(request,id):
    try:
        play=Play.objects.get(id=id)
        context = {
            "play":play
        }
    except play.DoesNotExist:
        raise Http404("No play found")
    return render(request,"play_detail.html",context=context)

def dvddetailview(request,id):
    try:
        dvd=Dvd.objects.get(id=id)
        context = {
            "dvd":dvd
        }
    except dvd.DoesNotExist:
        raise Http404("No dvd found")
    return render(request,"dvd_detail.html",context=context)















