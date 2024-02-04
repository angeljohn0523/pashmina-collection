
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<str:order_number>', views.checkout_success,
         name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
        name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 746861c14f393f9b9eef6d7f22c5fcbcdebe3f3d
