from django.urls import path
from .views import public_api, secure_api



urlpatterns = [
    path('public/', public_api, name='public_api'),
    path('secure/', secure_api, name='secure_api'),
]

