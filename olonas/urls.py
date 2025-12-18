from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_olona232_view),
	path('edit/<int:id_dadabe>/<int:id_bebe>/<int:id_olona>/', views.edit_olona_view),
	path('new_zanaka/<int:id_dadabe>/<int:id_bebe>/', views.new_zanaka_view),
	path('new_vady/<int:id_dadabe>/<int:id_bebe>/<int:id_tompony>/', views.new_vady_view),
	path('new_zafy/<int:id_dadabe>/<int:id_bebe>/<int:id_dada>/<int:id_neny>/', views.new_zafy_view),
	path('new_rar/<int:id_dadabe>/<int:id_bebe>/<str:lahy_vavy>/<str:dada_neny>/', views.new_rar_view),
]
