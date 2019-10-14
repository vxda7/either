from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=100)
    contentA = models.CharField(max_length=100)
    contentB = models.CharField(max_length=100)
    urlA = models.CharField(max_length=500)
    urlB = models.CharField(max_length=500)
    countA = models.IntegerField()
    countB = models.IntegerField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.CharField(max_length=200)
