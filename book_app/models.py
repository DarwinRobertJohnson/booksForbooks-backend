from django.db import models

# Create your models here.
class BookEntry(models.Model):
    user_name = models.CharField(default="Darwin D Dragon", max_length=30)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(null=True,max_length=30)
    book_status = models.BooleanField(default=False)