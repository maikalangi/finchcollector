from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finches_id>/', views.finches_detail, name='detail'),
    path('finches/create', views.FinchesCreate.as_view(), name="finches_create"),
    path('finches/<int:pk>/update', views.FinchesUpdate.as_view(), name="finches_update"),
    path('finches/<int:pk>/delete', views.FinchesDelete.as_view(), name="finches_delete"),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:toys_id>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create', views.ToysCreate.as_view(), name="toys_create"),
    path('toys/<int:pk>/update', views.ToysUpdate.as_view(), name="toys_update"),
    path('toys/<int:pk>/delete', views.ToysDelete.as_view(), name="toys_delete"),
]