from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class News(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, default='Anonimo')
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False, null=False)
    #image = models.ImageField(upload_to='noticias/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo