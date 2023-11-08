from django.urls import path
from .views import index,about,contact,video,remot,product, productdetailview,gamedetailview,remotdetailview,videodetailview,clientdetailview,playdetailview,dvddetailview

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('video/', video, name='video'),
    path('remot', remot, name='remot'),
    path('product/', product,name='product'),
    path('<int:id>', productdetailview, name='productDetail'),
    path('games/<int:id>', gamedetailview, name='gameDetail'),
    path('remot/<int:id>', remotdetailview, name='remotDetail'),
    path('video/<int:id>', videodetailview, name='videoDetail'),
    path('client/<int:id>', clientdetailview, name='clientDetail'),
    path('play/<int:id>', playdetailview, name='playDetail'),
    path('dvd/<int:id>', dvddetailview, name='dvdDetail')
]

