from django.urls import path
from . import views
from .views import SuccessView, ContactView

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
	  path('get_project/(?P<id>\d+)$', views.get_project),
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]
