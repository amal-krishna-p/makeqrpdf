from django.urls import path
from client import views
urlpatterns = [
    path("",views.index,name="index"),
    path("base",views.base,name="base"),
    path("signup",views.signup,name="signup"),
    path("clientregister",views.clientregister,name="clientregister"),
    path("adminchk",views.adminchk,name="adminchk"),
    path("clientlogin",views.clientlogin,name="clientlogin"),
    path("clienthome",views.clienthome,name="clienthome"),
    path("clientdata",views.clientdata,name="clientdata"),
    path("logoutclient",views.logoutclient,name="logoutclient"),
    
    

]
