from django.db import router
from django.urls import include, path
from . import views

urlpatterns = [
    # path('', include(router.urls)),
    path('profile/', views.user, name='user'),
    path('login/', views.login, name='login'),

]
