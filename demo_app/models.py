from django.db import models


def get_upload_path(instance, filename):
    if hasattr(instance, 'model'):
        model = instance.model.__class__._meta
        name = model.verbose_name_plural.replace(' ', '_')
    else:
        name = instance._meta.verbose_name
    return f'{name}/images/{filename}'



class VillaImage(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    model = models.ForeignKey('Villa', on_delete=models.CASCADE, related_name='image', null=True)


class ArticleImage(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    model = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='image')


class SiteHeaderItem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.title} - {self.slug}'


class RentCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.title}'


class Villa(models.Model):
    category = models.ForeignKey(RentCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, db_index=True)
    rating = models.FloatField(null=True)
    location = models.CharField(max_length=100, null=True)
    is_recommended = models.BooleanField(default=False)
    
    def get_rating_desc(self):
        if 3 <= self.rating < 4:
            return 'Normal'
        elif 4 <= self.rating < 4.5:
            return 'Good'
        elif 4.5 <= self.rating:
            return 'Exceptional'
    
    def __str__(self):
        return f'{self.name}'


class Tour(models.Model):
    category = models.ForeignKey(RentCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, db_index=True)
    desc = models.TextField(max_length=1000)
    
    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    category = models.ForeignKey(RentCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.title}'


class Bike(models.Model):
    category = models.ForeignKey(RentCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.title}'


class Promotion(models.Model):
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=300)
    
    category = models.ForeignKey(RentCategory, on_delete=models.SET_NULL, null=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)


class CustomerReview(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50, null=True)
    body = models.CharField(max_length=500)
    
    avatar = models.ImageField(upload_to=get_upload_path, null=True)
    
class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to=get_upload_path, null=True)
    