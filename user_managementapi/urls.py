from django.db import router
from django.urls import include, path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # path('', include(router.urls)),
    path('profile/', views.user, name='user'),
    path('login/', views.login, name='login'),

]