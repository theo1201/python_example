from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # prepoupulated_fields属性告诉Django通过输入的标题来填充slug字段
    prepopulated_fields = {'slug': ('title', )}
    # 同时，现在的author字段展示显示为了一个搜索控件，这样当你的用户量达到成千上万级别的时候比再使用下拉框进行选择更加的人性化
    raw_id_fields = ('author', )
    # 有个可以通过时间层快速导航的栏，该栏通过定义date_hierarchy属性出现。
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
