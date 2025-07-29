from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=255, unique=True, default='N/A')
    def __str__(self):
        return self.name

class Published(models.Model):
    date = models.DateField()
    def __str__(self):
        return str(self.date)

class News(models.Model):
    news_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.TextField()
    link = models.URLField()

    authors = models.ManyToManyField(Author, related_name="news")
    published_dates = models.ManyToManyField(Published, related_name="news")

    def __str__(self):
        return self.title
