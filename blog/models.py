from django.db import models
from django.utils import timezone


class Post(models.Model):    ##Object- Defines our model
    author = models.ForeignKey('auth.User') ## Properties
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): ## function/method
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title