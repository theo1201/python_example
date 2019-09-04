from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # ，在SQL数据库中会被转化成VARCHAR。
    title = models.CharField(max_length=250)
    # slug就是一个短标签，该标签只包含字母，数字，下划线或连接线。
    # 构建漂亮的，友好的URLs
    # 在相同的日期中Django会阻止多篇帖子拥有相同的slug
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # 这个字段定义了一个多对一（many-to-one）的关系,我们告诉Django一篇帖子只能由一名用户编写，一名用户能编写多篇帖子。
    author = models.ForeignKey(User, related_name='blog_posts')
    # 它是TextField，在SQL数据库中被转化成TEXT。
    body = models.TextField()
    # 们使用Djnago的timezone的now方法来设定默认值
    publish = models.DateTimeField(default=timezone.now)
    # 因为我们在这儿使用了auto_now_add当一个对象被创建的时候这个字段会自动保存当前日期。
    created = models.DateTimeField(auto_now_add=True)
    # 因为我们在这儿使用了auto_now，当我们更新保存一个对象的时候这个字段将会自动更新到当前日期。
    updated = models.DateTimeField(auto_now=True)
    # status：这个字段表示当前帖子的展示状态。我们使用了一个choices参数，这样这个字段的值只能是给予的选择参数中的某一个值。
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
                              
    objects = models.Manager() # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title
