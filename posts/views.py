from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from posts.forms import BlogPostForm
from posts.models import BlogPost


def template(request):
    return render(request=request, template_name="posts/index.html")


class BlogPostCreate(CreateView):
    template_name = "posts/create-post.html"
    form_class = BlogPostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class BlogPostDetailView(DetailView):
    template_name = "posts/post-detail.html"
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)
        context.update(time=timezone.now())
        return context


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "posts/post-update.html"


class BlogPostList(ListView):
    model = BlogPost
    context_object_name = 'posts_list'


class BlogPostUserView(ListView):
    template_name = 'posts/user-posts.html'

    def get_context_data(self, **kwargs):
        context = super(BlogPostUserView, self).get_context_data(**kwargs)
        context.update(slug=self.kwargs.get("slug"))
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return BlogPost.objects.filter(author__slug=slug)

