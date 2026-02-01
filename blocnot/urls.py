from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name='index'),
    path('add/', views.NoteCreateView.as_view(), name='add_note'),
    path('edit/<int:pk>/', views.NoteUpdateView.as_view(), name='edit_note'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='delete_note'),
    path('add-category/', views.CategoryCreateView.as_view(), name='add_category'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]