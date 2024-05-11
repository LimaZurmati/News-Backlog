from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    news_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_article"
    )
    news_image = CloudinaryField('image', default='placeholder')
    news_excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    news_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    released_status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='news_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.news_title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE,
                             related_name="comments")
    user_name = models.CharField(max_length=80)
    user_email = models.EmailField()
    Comment_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.Comment_content} by {self.user_name}"