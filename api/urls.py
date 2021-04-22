from django.urls import path, include
from . import views
from .views import getPhoneNumberRegistered, getPhoneNumberRegistered_TimeBased

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),
    
  ]