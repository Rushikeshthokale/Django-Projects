from django.urls import path
from cbapp import views
urlpatterns=[
    path('myview',views.MyView.as_view()),
    path('addstudent',views.AddStudent.as_view()),
    path('',views.StudentList.as_view()),
    path('delete/<sid>',views.DeleteStudent.as_view()),
    path('update/<sid>',views.UpdateStudent.as_view())
]