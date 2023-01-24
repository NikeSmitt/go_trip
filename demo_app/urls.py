from django.urls import path
import demo_app.views as views

app_name = 'demo_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
]