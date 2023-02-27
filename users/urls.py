from django.urls import path

from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('edit-account/', views.edit_account, name='edit-account'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
