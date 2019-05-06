
password = serializer.CharField(label='密码')
    字段中label将修改前端的显示。不设置label, 该表格titile默认显示为password

serializers.ModelSerializer 和serializers.Serializer 之间的选择：
```
当明显的需要序列化的内容在Model中已经定义那么我们用ModelSerializer.
没有定义Model且需要序列化工作的使用Serializer.

使用ModelSerializer时，也可以序列化非Model中的临时字段。
结合write_only、read_only、覆盖validate方法: def attrs['xx']


```

Serializer中自定义字段的验证方法， validated_code(self, code)

Serializer中在字段定义阶段的初步验证。error_messages= {}