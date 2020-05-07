from django.urls import path
from . import views


urlpatterns=[
	path('',views.AccountView.as_view(),name='account'),
	path('/signin',views.SignInView.as_view(),name='signin'),
]
