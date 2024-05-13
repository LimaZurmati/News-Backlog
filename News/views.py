from django.shortcuts import render
from django.views import generic
from .models import News

# Create your views here.
class NewsList(generic.ListView):
    model = News
    queryset = News.objects.filter(
    released_status=1).order_by("-created_on")
    print('QUERY: ', queryset)
    template_name = "index.html"
    paginate_by = 6