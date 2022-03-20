from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    updateDate = models.DateTimeField(auto_now=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
     card = models.ForeignKey(Card,on_delete=models.CASCADE,related_name="comments")
     comment =models.CharField(max_length=150)
     createdDate = models.DateTimeField(auto_now_add=True)
     user = models.ForeignKey(User,on_delete=models.CASCADE)

     def __str__(self):
        return f'{self.card}'
class Likes(models.Model):
     card = models.ForeignKey(Card,on_delete=models.CASCADE,related_name="likes")
     user = models.ForeignKey(User,on_delete=models.CASCADE)

     def __str__(self):
        return f'{self.card}'




 