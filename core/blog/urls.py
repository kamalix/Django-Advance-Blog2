from django.urls import path
from django.views.generic import TemplateView
from .views import IndexView

urlpatterns = [
    path('fbv-index', IndexView,name='fbv-index'),
    path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context = {'name':'ali'})),
]