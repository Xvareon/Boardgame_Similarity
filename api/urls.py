from django.urls import path
from .views import similarity_view, similar_users_view

urlpatterns = [
    path('similarity/', similarity_view, name='similarity'),
    path('similar-users/', similar_users_view, name='similar_users'),
]