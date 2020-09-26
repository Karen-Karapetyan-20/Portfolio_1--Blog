from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime as dt


class Article(models.Model):
    CATEGORY = (
        ("Notebooks", "Notebooks"),
        ("Smartphones", "Smartphones"),
        ("Cars", "Cars"),
        ("Cameras", "Cameras"),
        ("Home appliances", "Home appliances"),
        ("Apartments", "Apartments"),
        ("Other", "Other")
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=50, choices=CATEGORY)
    article_taken = models.URLField(max_length=500, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to="users/article/images")
    video = models.FileField(upload_to="users/article/videos", blank=True, null=True)
    publish_date = models.DateTimeField(default=dt.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-publish_date"]
