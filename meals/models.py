from django.db import models
from django.utils.text import slugify
# Create your models here.


class Meals(models.Model):
    name = models.CharField(max_length=50,verbose_name="نام")
    description = models.TextField(max_length=500,verbose_name="توضیحات")
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True,verbose_name="دسته بندی")
    people = models.IntegerField(verbose_name="نفرات")
    price = models.DecimalField(max_digits=5 , decimal_places=2,verbose_name="قیمت")
    preperation_time =models.IntegerField(verbose_name="زمان حاظر شدن")
    image = models.ImageField(upload_to='meals/',verbose_name="تصویر")
    slug = models.SlugField(blank=True, null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Meals , self).save(*args , **kwargs)



    class Meta:
        verbose_name = 'وعده غذایی'
        verbose_name_plural = 'وعده غذایی ها'


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="دسته بندی")


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name





