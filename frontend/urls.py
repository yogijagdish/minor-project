from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('trek',views.trek),
    path('guide',views.guide),
    path('contactus/',views.contact_us),
    path('curentrecord',views.curent_record),
    path('trek/tilicho',views.tilicho),
    path('trek/langtang',views.langtang),
    path('trek/mardi',views.mardi),
    path('current/trekker1',views.trekker1)

]