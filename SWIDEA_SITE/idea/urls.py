from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'idea'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    #devtool
    path('devtools/', devtool_list, name='devtool_list'),
    path('create/devtool/', add_devtool, name='create_devtool'),
    path('detail/devtool/<int:pk>/', detail_devtool, name='detail_devtool'),
    path('delete/devtool/<int:pk>/', delete_devtool, name='delete_devtool'),
    path('update/devtool/<int:pk>/', update_devtool, name='update_devtool'),
    path('toggle_star/', toggle_star, name='toggle_star'),
    path('change_interest/', change_interest, name='change_interest'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)