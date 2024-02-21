from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.list import ListView
from .models import Post


# Create your views here.
'''
#Function based view show a template
def IndexView(request):
     """
     a function based view to show index page
     """
     context={'name':'ali'}
     return render(request,"index.html",context)
'''


class IndexView(TemplateView):
    '''
    a function based view to show index page
    '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context

'''FBV for redirect   
def RedirectToMaktab(request):
    return redirect("https://www.maktabkhooneh.com")
'''


class RedirectToMaktab(RedirectView):
    url = 'https://www.maktabkhooneh.com'
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

class PostList(ListView):
    #model = Post
    #queryset = Post.objects.all()
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts
    context_object_name = 'posts'











