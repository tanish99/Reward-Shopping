from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.rewards import RewardView
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.profile import ProfileView
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('rewards' ,auth_middleware(RewardView.as_view()), name='rewards'),
    path('profile' ,auth_middleware(ProfileView.as_view()), name='profile')
]
