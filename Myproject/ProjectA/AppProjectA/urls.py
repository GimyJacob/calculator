from . import views
from django.urls import path
app_name='AppProjectA'

urlpatterns = [
    path('',views.home,name='home'),
   # path('about/',views.about,name='about'),
    path('result/',views.result,name='result'),
    path('thanks/',views.thanks,name='thanks'),
    path('manipulation/',views.manipulation,name='manipulation'),
    path('index/',views.index,name='index')

]