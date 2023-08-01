from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from phoneData import views

router = DefaultRouter()
router.register('phoneData',views.PhoneDataViewSet)
urlpatterns=[
    path('',include(router.urls)),
]
