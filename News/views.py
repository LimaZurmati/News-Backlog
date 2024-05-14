from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import News

# Create your views here.
class NewsList(generic.ListView):
    model = News
    queryset = News.objects.filter(
    released_status=1).order_by("-created_on")
    print('QUERY: ', queryset)
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = News.objects.filter(released_status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user_name.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )

        