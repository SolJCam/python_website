from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=150)
    github_url = models.CharField(max_length=100)
    image = models.FilePathField(path="main/static/img")
    def __str__(self): #string magic-method to return title as string - an obviously more helpful representation of this object
        return self.title


class Word(models.Model):
    word = models.CharField(max_length=20)
    definition = models.TextField()
    second_definition = models.TextField(blank=True, null=True)
    more_definitions = models.TextField(blank=True, null=True)
    creator = models.PositiveSmallIntegerField(blank=True, null=True)
    def __str__(self): #string magic-method to return name as string
        return self.word+": "+self.definition+", "+self.second_definition+", "+self.more_definitions+", "+str(self.creator)

# class Word(models.Model):
#     word = models.CharField(max_length=20)
#     definition = models.TextField(max_length=120)
#     example = models.CharField(max_length=120, blank=True)
#     second_definition = models.TextField(max_length=120, blank=True)
#     second_ex = models.CharField(max_length=120, blank=True)
#     third_definition = models.TextField(max_length=120, blank=True)
#     third_ex = models.CharField(max_length=120, blank=True)
#     synonym = models.CharField(max_length=120, blank=True)
#     more_definitions = models.TextField(blank=True)
#     creator = models.PositiveSmallIntegerField(blank=True, null=True)
#     def __str__(self): #string magic-method to return name as string
#         return self.word+": "+self.first_definition+", "+self.first_ex+", "+self.second_definition+", "+self.second_ex+", "+self.third_definition+", "+self.third_ex