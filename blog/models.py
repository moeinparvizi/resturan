from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا")
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/'  , blank=True, null=True,verbose_name="تصویر")
    # tags
    category = models.ForeignKey('Category'  ,null=True, on_delete=models.SET_NULL,verbose_name="دسته بندی")
    created  = models.DateTimeField(default=timezone.now)

    tags = TaggableManager(blank=True)


    class Meta:
        verbose_name = ' پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title



class Category(models.Model):
    category_name = models.CharField(max_length=50)


    class Meta:
        verbose_name = ' دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.category_name



class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,verbose_name="کاربر")
    post = models.ForeignKey(Post , on_delete=models.CASCADE,verbose_name="پست")
    content = models.TextField(verbose_name="محتوا")
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = ' کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return str(self.content)