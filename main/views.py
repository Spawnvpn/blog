from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from main.forms import BlogPostForm
from main.models import BlogPost


def template(request):
    return render(request=request, template_name="main/index.html")


class BlogPostCreate(CreateView):
    template_name = "main/create-post.html"
    form_class = BlogPostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class BlogPostDetailView(DetailView):
    template_name = "main/post-detail.html"
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)
        context.update(time=timezone.now())
        return context


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "main/post-update.html"


class BlogPostList(ListView):
    model = BlogPost
    context_object_name = 'posts_list'

