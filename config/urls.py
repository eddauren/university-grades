"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from academics.views import StudentViewSet, EnrollmentViewSet, set_grade, top_students
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

router= DefaultRouter()
router.register("students", StudentViewSet)
router.register("enrollments", EnrollmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/set-grade/', set_grade),
    path('api/top-students/', top_students),
    path('api/token/', obtain_auth_token)
]
