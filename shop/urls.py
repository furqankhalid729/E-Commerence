from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from.import views

from .views import *

urlpatterns = [
    path('',views.store,name='home'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('about/',views.about,name='about'),
    path('contactus/', views.contact, name='ContactUs'),
    path('productView/<int:pk>', view.as_view(), name='p_view'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('profile/<int:pk>',profile.as_view(),name='profile'),
    path(r'update_cart/<P_id>',views.update_cart,name='update_carts'),
    path(r'update_carts/<id>',views.update_cart_product,name='update_cart'),
    path(r'inc_quan/<id>',views.inc_quan,name='inc_quan'),
     path(r'rem_quan/<id>',views.rem_quan,name='rem_quan'),
    path('remove/<id>',views.remove_product,name='remove'),
    path('change_pass/',views.change_pass,name='change_pass'),
    path('rest_password',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('rest_password_sent',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('rest/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('rest_change',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]