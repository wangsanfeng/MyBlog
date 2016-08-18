#coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class BlogArticle(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null = True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']

    #获取URL并转换成url的表示形式
    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
