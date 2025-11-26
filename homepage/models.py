from django.db import models




class newtours(models.Model):
    place = models.CharField(max_length=100)
    budject = models.CharField(max_length=50)
    items = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to='static/images', default='')
    img2 = models.ImageField(upload_to='static/images', default='')
    img3 = models.ImageField(upload_to='static/images', default='')
    img4 = models.ImageField(upload_to='static/images', default='')
    img5 = models.ImageField(upload_to='static/images', default='')
    
    def __str__(self):
        return str(self.id)+ ':' +self.place