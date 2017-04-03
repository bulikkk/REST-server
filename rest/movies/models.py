from django.db import models




class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
#     def get_absolute_url(self):
        
  

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey('Person', related_name='director')
    actors = models.ManyToManyField('Person', through='Role')
    year = models.IntegerField(null=True)
    
    def __str__(self):
        return "{} || {}".format(self.title, self.year)
        
  
class Role(models.Model):
    person = models.ForeignKey('Person', related_name='actor')
    movie = models.ForeignKey('Movie', related_name='movie')
    role = models.CharField(max_length=128)
    
    def __str__(self):
        return 'Actor: {} as {} in {}'.format(self.person, self.role, self.movie)
      

