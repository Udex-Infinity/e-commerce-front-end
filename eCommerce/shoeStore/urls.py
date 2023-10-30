from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:shoe_name>",views.details,name='details'),
    path("<str:shoe_name>/payment",views.payment,name="payment")
]