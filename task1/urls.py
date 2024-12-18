from django.urls import path
from .views import index, games, cart, registration

urlpatterns = [
    path('', index, name='index'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
    path('registration/', registration, name='registration'),
]