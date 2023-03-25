from django.urls import path
from company import views
from .views import CompanyAPIView, CompanyList, EmployeeList, EmployeeDetail, CompanyEmployeesList
urlpatterns = [
    path("", views.home, name="home"),
    path('companies/', CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyAPIView.as_view(), name='company-detail'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('companies/<int:company_id>/employees/', views.CompanyEmployeesList.as_view()),

]