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
    # class Meta:
    #     db_table = 'main_projects'


class Word(models.Model):
    word = models.CharField(max_length=120)
    first_definition = models.TextField(max_length=250)
    first_ex = models.CharField(max_length=120, blank=True)
    second_definition = models.TextField(max_length=250, blank=True)
    second_ex = models.CharField(max_length=120, blank=True)
    third_definition = models.TextField(max_length=250, blank=True)
    third_ex = models.CharField(max_length=120, blank=True)
    synonym = models.CharField(max_length=120, blank=True)
    more_definitions = models.TextField(blank=True)
    creator = models.PositiveSmallIntegerField(blank=True, null=True)
    def __str__(self): #string magic-method to return name as string
        return self.word+": "+self.first_definition+", "+self.first_ex+", "+self.second_definition+", "+self.second_ex+", "+self.third_definition+", "+self.third_ex
    # class Meta:
    #     db_table = 'main_word'

    # def random_string(self):
    #     pool = string.ascii_letters + string.digits
    #     self.unique_hash = ''.join(random.choice(pool) for i in range(8))
    #     return self.unique_hash