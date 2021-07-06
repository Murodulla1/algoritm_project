from django.urls import path
from .views import shart_list, bajar_list, shart_post, bajar_post

urlpatterns = [
    path('shart/', shart_list),
    path('shart/<int:pk>/', shart_post),
    path('bajar/', bajar_list),
    path('bajar/<int:pk>/', bajar_post),

]
