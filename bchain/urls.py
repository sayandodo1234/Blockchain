from django.urls import path
from .import views
from django.views.generic import TemplateView

urlpatterns=[
    path('index/',views.index,name="index"),
    path('getdata/',views.get_data , name="getdata"),
    path('viewdata/',views.show_data,name="viewdata"),
    path('node/',views.register_nodes,name='node'),
    path('shownode/',views.show_nodes,name='shownode'),
    path('announce/',views.announce_block,name='announce'),
    path('receiveblock/',views.receive_block,name='receive'),
]
