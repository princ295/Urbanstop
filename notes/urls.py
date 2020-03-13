from django.contrib import admin
from django.urls import path, include


from notes import views

urlpatterns = [

    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

    path('notelist/', views.NotesListView.as_view(), name=views.NotesListView.name),
    path('notelist/<int:pk>', views.NoteDetailView.as_view(), name=views.NoteDetailView.name),

    path('user/<int:pk>', views.UserDetailView.as_view(), name=views.UserDetailView.name),

    path('filterupdatedate/', views.filterbydate.as_view(), name= views.filterbydate.name)
   
]