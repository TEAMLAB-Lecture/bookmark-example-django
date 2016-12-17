from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    bookmark_name = models.CharField(max_length=100)
    bookmark_url = models.CharField(max_length=255)
    bookmark_desc = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_id =  models.AutoField(primary_key=True)
    comment_contents = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True)