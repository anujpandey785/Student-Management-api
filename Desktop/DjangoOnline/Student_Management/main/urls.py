from django.urls import path
from main import views

urlpatterns = [
    path('',views.Index.as_view()),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name='college'),
    path('college/', views.Collegelist.as_view()),
    path('createcollege/', views.CollegeCreate.as_view()),
    path('createstudent/', views.StudentCreate.as_view()),
    path('updatecollege/<int:pk>', views.CollegeUpdate.as_view()),
    path('deletestudent/<int:pk>', views.StudentDelete.as_view()),
]