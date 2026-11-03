from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_view, name="home"),
    #path("save_pay_records/",views.save_pay_records, name="save_pay_records"),
]
