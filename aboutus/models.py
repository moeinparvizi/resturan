from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length = 50,verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    # image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'دریاره ما'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return self.title


class Why_Choose_Us(models.Model):
    title = models.CharField(max_length=50,verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")

    class Meta:
        verbose_name = 'چرا ما را انتخوای کنید'
        verbose_name_plural = 'چرا ما را انتخوای کنید'

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50,verbose_name="نام")
    title = models.CharField(max_length=50,verbose_name="عنوان")
    bio = models.TextField(verbose_name="بیوگرافی")
    image = models.ImageField(upload_to='chef/',verbose_name="تصاویر")

    class Meta:
        verbose_name = 'آشپز'
        verbose_name_plural = 'آشپز'

    def __str__(self):
        return self.name