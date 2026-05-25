from django.urls import path
from . import views
from . import auth_views

app_name = 'notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('level/<slug:slug>/', views.level_detail, name='level_detail'),
    path('chapter/<slug:slug>/', views.chapter_detail, name='chapter_detail'),
    path('note/<slug:slug>/', views.note_detail, name='note_detail'),

    # Auth
    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
]