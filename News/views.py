from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import News
from .forms import CommentForm

# Create your views here.
class NewsList(generic.ListView):
    model = News
    queryset = News.objects.filter(
    released_status=1).order_by("-created_on")
    print('QUERY: ', queryset)
    template_name = "index.html"
    paginate_by = 6


class NewsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = News.objects.filter(released_status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "news_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = News.objects.filter(released_status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "news_details.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )        

        