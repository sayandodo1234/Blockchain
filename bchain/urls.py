from django.urls import path
from .import views
from django.views.generic import TemplateView

urlpatterns=[
    path('index/',views.index,name="index"),
    path('getdata/',views.get_data , name="getdata"),
    path('viewdata/',views.show_data,name="showdata"),
    path('thanks/',views.thankpage,name='thankyou'),
]
