from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    rate = models.IntegerField()
    blog_content = models.TextField()

    def __str__(self):
        return self.title

class TravelReview(models.Model):
    title = models.CharField(max_length=255)
    restaurant_rating = models.PositiveIntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
    hotel_rating = models.PositiveIntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
    transportation_rating = models.PositiveIntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
    sightseeing_rating = models.PositiveIntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
    locals_rating = models.PositiveIntegerField(default=0, choices=[(i, str(i)) for i in range(6)])
    restaurant_name = models.CharField(max_length=255)
    hotel_name = models.CharField(max_length=255)
    transportation_comment = models.TextField()
    sightseeing_comment = models.TextField()
    locals_comment = models.TextField()
    blog_content = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    # other fields if needed
    # ...

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username
