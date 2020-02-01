from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """图书信息模型类"""
    # 馆藏地址
    baddress = models.CharField(max_length=20)
    # 书名
    bname = models.CharField(max_length=20)
    # 图书与读者的关系
    breader = models.ForeignKey('ReaderInfo', on_delete=models.CASCADE)

    def __str__(self):
        """返回书名"""
        return self.bname

    class Meta:
        db_table = ''


class ReaderInfo(models.Model):
    """读者信息模型类"""
    # 读者号
    rid = models.CharField(max_length=20)
    # 读者名
    rname = models.CharField(max_length=20)

    def __str__(self):
        """返回读者号"""
        return self.rid

