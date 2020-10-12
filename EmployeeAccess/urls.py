from django.urls import path
from .views import EmployeeAPIView    # import employee view class


urlpatterns = [
    path('status/', EmployeeAPIView.as_view()),  # url path for predict access status with serializer
    ]
