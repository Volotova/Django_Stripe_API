from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('item/<int:pk>', ItemPageView.as_view(), name='item'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]
