from rest_framework import serializers

from booktest.models import BookInfo


# class BookInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookInfo
#         fields = '__all__'


class BookInfoModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer 1.可以自动根据模型生成序列器中的字段 2.帮我们实现了序列化器中的create 和update
    """
    # heroinfo_set = HeroInfoSerializer(many=True)
    class Meta:
        model = BookInfo  # 将来自动生成序列化器字段时,字段从BookInfo模型中生成
        fields = "__all__"  # 指定映射BookInfo模型中所有字段
        # fields = ['id', 'btitle', 'bpub_date']  # 指定要映射的模型字段
        # exclude = ['image']  # 除了指定的字段不需要其它全生成
        # read_only_fields = ['bread', 'bcomment']  # 指定那些字段只做序列化的输出
        extra_kwargs = {
            'bread': {'min_value': 0, 'required': True}
        }

# 在字段中添加validators选项参数，也可以补充验证行为
# def about_django(value):
#     if 'django' not in value.lower():
#         raise serializers.ValidationError("图书不是关于Django的")


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20, required=True)
    bpub_date = serializers.DateField(label='发布日期', required=True)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)


    # def validate_btitle(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("图书不是关于Django的")
    #     return value

    # def validate(self, attrs):
    #     bread = attrs['bread']
    #     bcomment = attrs['bcomment']
    #     if bread < bcomment:
    #         raise serializers.ValidationError('阅读量小于评论量')
    #     return attrs
    """
    如果创建序列化器对象的时候，没有传递instance实例，则调用save()方法的时候，
    create()被调用，相反，如果传递了instance实例，则调用save()方法的时候，update()被调用。
    """
    def create(self, validated_data):
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    # 只会序列化关联对象的主键
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())
    hbook = serializers.StringRelatedField(label='书籍', read_only=True)  # 序列化关联对象的__str__
    # hbook = BookInfoSerializer()  # 指定关联序列化器实例对象