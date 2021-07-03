from django.urls import path
from . import views
urlpatterns=[path('',views.index,name="index"),
path('paymentform/<int:price>/<path:link>/<str:productname>',views.paymentform,name='paymentform'),]