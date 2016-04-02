from django.conf.urls import url
import views


# TEST COMMENT

urlpatterns = [
    url(r"^$", view=views.template),
    url(r"^post/create/$", view=views.BlogPostCreate.as_view(), name="post-create"),
    url(r"^post/(?P<pk>\d+)/$", view=views.BlogPostDetailView.as_view(), name="post-detail"),
    url(r"^post/(?P<pk>\d+)/update/$", view=views.BlogPostUpdateView.as_view(), name="post-update"),
    url(r"^posts/all/$", view=views.BlogPostList.as_view(), name="blogpost_list"),
    url(r"^(?P<slug>\w+)/posts/$", view=views.BlogPostUserView.as_view(), name="user-posts")
]
