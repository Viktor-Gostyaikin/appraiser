from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('file/<file>/', views.file_tf_idf, name='file_tf_idf'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('delete/<id>', views.delete_file, name='delete')
]