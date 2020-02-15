from django.urls import path
from . import views

app_name='user_profile'

urlpatterns= [
    path('',views.IndexView.as_view(),name='index'),
    path('foo/',views.FooViews.as_view(),name='foo'),
path('bar/<int:pk>/',views.BarViews.as_view(),name='bar')
]
