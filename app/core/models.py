from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'city'

class Advert(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    city = models.ForeignKey(City, related_name='city_adverts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='category_adverts')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'advert'
