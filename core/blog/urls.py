from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.views.generic.base import RedirectView



app_name = "blog"


urlpatterns = [
    path('cbv-index/',views.IndexView.as_view(),name='cbv-index'),
    path('post/',views.PostList.as_view(),name='post-list'),
    path('go-to-maktabkhooneh/<int:pk>/', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
]