from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('update/<int:no>', views.update , name='update'),
    path('detail/<int:no>', views.detail, name='detail'),
    path('detail/<int:no>/delete', views.delete , name='delete'),
]