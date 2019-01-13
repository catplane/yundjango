from django.shortcuts import render

# Create your views here.

# Create your views here.
from booktest.models import BookInfo, HeroInfo
from django.db.models import F, Q, Sum

"""新增操作"""
# 新增一本书
# book = BookInfo()
# book.btitle = '西游记'
# book.bpub_date = '1991-11-11'
# book.save()

# book = BookInfo(
#     btitle='红楼梦',
#     bpub_date='2000-11-11'
# )
# book.save()

# 用create创建模型时,不用再调用save,创建的同时直接保存
# book = BookInfo.objects.create(
#     btitle='红楼梦',
#     bpub_date='2000-11-11'
# )

# hero = HeroInfo.objects.create(
#     hname='白骨精',
#     hbook=book,
#     # hbook_id=book.id,
# )


"""基本查询"""
# get  all  count
# try:
#     book = BookInfo.objects.get(id=10)
# except BookInfo.DoesNotExist:
#     pass

# BookInfo.objects.all()
# BookInfo.objects.all().count()


"""过滤查询"""
BookInfo.objects.filter(id=1)
# BookInfo.objects.filter(id__exact=1)
BookInfo.objects.filter(btitle__contains='湖')
BookInfo.objects.filter(btitle__endswith='部')
BookInfo.objects.filter(btitle__isnull=False)
BookInfo.objects.filter(id__in=[2, 4])
# gt > gte >=  lt < lte <=
BookInfo.objects.filter(id__gt=2)

BookInfo.objects.exclude(id=3)

BookInfo.objects.filter(bpub_date__year='1980')

BookInfo.objects.filter(bpub_date__gt='1990-1-1')

"""F对象和Q对象"""
# 如果需要做两个字段进行比较就要用F
BookInfo.objects.filter(bread__gt=F('bcomment'))
BookInfo.objects.filter(bread__gt=F('bcomment') * 2)

# Q对象可以做逻辑运算符 and  or  not  可以做基本查询 也可以 or 或 not
# BookInfo.objects.filter(bread__gt=20, id__lte=3)  # and表示两个条件都满足的才要
# BookInfo.objects.filter(Q(bread__gt=20), Q(id__lte=3))

BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))  # or 满足其中一个条件的就要
BookInfo.objects.filter(~Q(id=3))

"""
只要给多的一方指定的外键,那么在一的那方就会隐式生成一个隐藏字段: 多的那一方模型名小写_set  heroinfo_set
"""

"""基本关联查询
一查多:  用book去查hero
第一步先拿到一:book
第二完成一查多: 一的模型实例对象.多的模型名字小写_set  book.heroinfo_set

多查一
第一步先拿到多的这一方的某个模型对象  hero
第二步 hero.hbook
"""
# book = BookInfo.objects.get(id=1)
# book.heroinfo_set.all()
#
# hero = HeroInfo.objects.get(id=1)
# hero.hbook

"""关联过滤/内联查询"""
# 一查多:  查谁就是谁的模型类对象开头.objects.filter(外键名__属性名__运算符=值)
# HeroInfo.objects.filter(hbook__btitle='天龙八部')

"""在关联过滤查询时多的一方当条件时,只用写多的一方模型名小写就可以了,不用再加_set 

_set 是在关联基本查询时,用一查多才需要用"""
# 多查一: 用一这方的模型类对象.objects.filter(多的那一方模型名小写__属性名__运行符=值)
BookInfo.objects.filter(heroinfo__hcomment__contains='降龙')

# 只能对QuerySet类型的东西进行排序
# BookInfo.objects.all().order_by('bread')  # 默认升序
# BookInfo.objects.all().order_by('-bread')  # 降序


# BookInfo.objects.aggregate(Sum('bread'))


"""数据修改"""
# book = BookInfo.objects.get(btitle='西游记')
# book.btitle = '西游记<后传>'
# book.save()
#
#
# BookInfo.objects.filter(id=5).update(btitle='西游记<起源>')

"""数据删除"""
book = BookInfo.objects.get(id=5)
book.delete()

HeroInfo.objects.filter(id=18).delete()

qs = BookInfo.objects.all()

# qs1 = BookInfo.objects.all()
