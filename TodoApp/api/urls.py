from django.urls import path
from . import views


urlpatterns = [
    path('createTodo', views.createTodo),
    path('todoList', views.todoList),
    path('update/<str:pk>/', views.updateTodo),
    path('delete/<str:pk>/', views.delete)
]

todo1 = {
    "title":"Finish design for todoapp",
    "description":"add color to mockup design and export"
}

todo2 = {
    "title":"Host python project on vercel",
    "description":"Commit project files to github and deploy to vercel"
}

todo3 = {
    "title":"Learn Docker",
    "description":"Search for a good docker tutorial on youtube"
}