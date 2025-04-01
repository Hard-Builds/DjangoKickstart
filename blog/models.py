from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from blog.enum import PostStatusEnum


class AvailPosts(models.Manager):
    def published(self):
        return super().get_queryset().filter(status=PostStatusEnum.PUBLISHED.value)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=100,
        default=PostStatusEnum.PUBLISHED.value,
        choices=PostStatusEnum.choices()
    )

    objects = AvailPosts()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-details", kwargs={"pk": self.pk})
