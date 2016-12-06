from django.db import models

class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    bookmark_name = models.CharField(max_length=100)
    bookmark_url = models.CharField(max_length=255)
