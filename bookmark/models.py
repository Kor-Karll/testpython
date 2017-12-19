from django.db import models

class Bookmark(models.Model):
    #기본키(PK)
    id = models.AutoField(primary_key = True)
    #북마크 제목
    title = models.CharField(null = True,max_length = 100)
    #북마크URL
    url = models.URLField(unique = True)

# Create your models here.
