from django.urls import path
from . import views
app_name = 'main_page'
urlpatterns=[
    path('',view=views.landing_page,name="landing_page")
]