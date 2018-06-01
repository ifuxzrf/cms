from django.db import models


# Create your models here.

class Things(models.Model):
    name = models.CharField(max_length=30, blank=True)
    price = models.CharField(max_length=30, blank=True)


class image(models.Model):
    thing = models.ForeignKey("Things", on_delete=models.CASCADE)
    imgge_path = models.CharField(max_length=30, blank=True)

#
# class Book(models.Model):
#     nid = models.AutoField(primary_key=True)  # 自增id(可以不写，默认会有自增id)
#     title = models.CharField(max_length=32)
#     publishDdata = models.DateField()  # 出版日期
#     price = models.DecimalField(max_digits=5, decimal_places=2)  # 一共5位，保留两位小数
#
#     # 一个出版社有多本书，关联字段要写在多的一方
#     # 不用命名为publish_id，因为django为我们自动就加上了_id
#     publish = models.ForeignKey("Publish")  # foreignkey（表名）建立的一对多关系
#     # publish是实例对象关联的出版社对象
#     authorlist = models.ManyToManyField("Author")  # 建立的多对多的关系
#
#     def __str__(self):  # __str__方法使用来吧对象转换成字符串的，你返回啥内容就打印啥
#         return self.title
#
#
# class Publish(models.Model):
#     # 不写id的时候数据库会自动给你增加自增id
#     name = models.CharField(max_length=32)
#     addr = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.name
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=32)
#     age = models.IntegerField()
#
#
# class AuthorDeital(models.Model):
#     tel = models.IntegerField()
#     addr = models.CharField(max_length=32)
#     author = models.OneToOneField("Author")  # 建立的一对一的关系
#
#
# # 一对多的添加
# # 方式一:如果是这样直接指定publish_id字段去添加值，前提是你的主表里面必须有数据
# # 主表：没有被关联的（因为book表是要依赖于publish这个表的）也就是publish表
# # 子表：关联的表
# Book.objects.create(title="追风筝的人", publishDdata="2015-5-8", price="111", publish_id=1)
# # 方式二:推荐
# pub_obj = Publish.objects.filter(name="人民出版社")[0]
# print(pub_obj)
# Book.objects.create(title="简爱", publishDdata="2000-6-6", price="222", publish=pub_obj)
#
# # 方式三：save
# pubObj = Publish.objects.get(name="人民出版社")  # 只有一个的时候用get,拿到的直接就是一个对象
# bookObj = Book(title="真正的勇士", publishDdata="2015-9-9", price="50", publish=pubObj)
# bookObj.save()
