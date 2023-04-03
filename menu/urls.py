from django.urls import path
from .views import MenuViev


urlpatterns = [
    path("menu/", MenuViev.as_view(), name="menu_page")
]
