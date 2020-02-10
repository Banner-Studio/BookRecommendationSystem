from django.contrib import admin
from data.models import BookInfo, ReaderInfo
# Register your models here.


class BookInfoStackedInline(admin.StackedInline):
    # 写多类的名字
    model = BookInfo
    # extra = 2
    # raw_id_fields = ("breader",)
    fk_name = 'breader'


class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类 """
    list_display = ['id', 'bname', 'baddress', 'breader']
    # list_filter = ['bname']  # 列表页右侧过滤栏
    search_fields = ['bname', 'baddress', 'breader__rid']  # 列表页上方的搜索栏
    # readonly_fields = ('id', 'breader')
    ordering = ('baddress', 'breader')


class ReaderInfoAdmin(admin.ModelAdmin):
    """读者模型管理类"""
    list_display = ['id', 'rid', 'rname']
    inlines = [BookInfoStackedInline]
    search_fields = ['rid']  # 列表页上方的搜索栏
    ordering = ('rid',)
    # readonly_fields = ('id',)


# #注册模型类

admin.site.register(ReaderInfo, ReaderInfoAdmin)


admin.site.register(BookInfo, BookInfoAdmin)

