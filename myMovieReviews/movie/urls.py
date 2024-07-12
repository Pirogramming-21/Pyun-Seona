from django.urls import path
from .views import *

urlpatterns = [
    path('', review_list, name='review_list'),
    path('write', add_review, name='review_write'),
    path('detail/<int:id>/', review_detail, name='review_detail'), 
    path('update/<int:id>/', review_update, name='review_update'),
    path('delete/<int:id>/', review_delete, name='review_delete'),
]
