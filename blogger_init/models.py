from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    last_login_time = models.DateTimeField('last login')
    user_create_time = models.DateTimeField('date joined')

class Blog(models.Model):
    blog_id = models.CharField(max_length = 200)
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    upvotes = models.IntegerField()

class Comment(models.Model):
    comment_id = models.CharField(max_length = 200)
    blog = models.ForeignKey(Blog)
    user = models.ForeignKey(User)
    text = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
