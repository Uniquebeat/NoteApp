from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView, name='noteList'),
    path('noteDetail/<int:pk>', views.NoteDetailView, name='noteDetail'),
    path('noteCreate/', views.NoteCreateView, name='noteCreate'),
    path('noteDelete/<int:pk>', views.NoteDeleteView, name='noteDelete')
]