





from django.conf.urls import url
from . import views




urlpatterns = [


    url(r'^index/$', views.index, name = "index"),
    
    url(r'^item/(?P<item_id>\d+)/$', views.item, name = "item"),
    #url(r'^$', views.index),
    #
    #
    #url(r'^chat', HomeView.as_view(), name = 'chat'),
    #
    #url(r'^home/$', views.home, name = "home"),
    #url(r'^payment/$', views.payment, name = "payment"),
    #url(r'^hasira/$', views.hasira, name = "hasira"),
    #url(r'^index/$', views.index, name = "index"),
    #
    #url(r'^item/(?P<item_id>\d+)/$', views.item, name = "item"),
    #
    #url(r'^himaya/$', views.himaya, name = "himaya"),
    #url(r'^item2/(?P<item_id>\d+)/$', views.item2, name = "item2"),
    #
    #url(r'^register/$', views.register, name = "register"),
    #url(r'^image/$', views.image, name = "image"), 
    #
    #
    #url(r'^class/$', views.classes_home, name = "class"),
    #url(r'^make/$', views.classes_create, name = "make"),
    #url(r'^detail/(?P<id>\d+)/$', views.classes_detail, name = "detail"),
    #url(r'^detail/(?P<id>\d+)/edit/$', views.classes_update, name = "update"),
    #url(r'^detail/(?P<id>\d+)/delete/$', views.classes_delete, name = "delete"),  
]