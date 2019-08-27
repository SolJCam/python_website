from django.db import models
import random, string

# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=20)
    first_definition = models.CharField(max_length=120)
    first_ex = models.CharField(max_length=120, blank=True)
    second_definition = models.CharField(max_length=120, blank=True)
    second_ex = models.CharField(max_length=120, blank=True)
    third_definition = models.CharField(max_length=120, blank=True)
    third_ex = models.CharField(max_length=120, blank=True)
    unique_hash = models.CharField(max_length=8)
    def __str__(self): #return a more helpful representation of this object
        return self.name, self.first_definition, self.first_ex, self.second_definition, self.second_ex, self.third_definition, self.third_ex

    # def random_string(self):
    #     pool = string.ascii_letters + string.digits
    #     self.unique_hash = ''.join(random.choice(pool) for i in range(8))
    #     return self.unique_hash
        