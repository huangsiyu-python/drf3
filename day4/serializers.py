from rest_framework import serializers
from api.models import Book

class BookListSeralizer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        for index,obj in enumerate(instance):
            self.child.update(obj,validated_data[index])
        return instance

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=("book_name","price","publish","authors","pic")
        extra_kwargs={
            "book_name":{
                "required":True,
                "min_length":3,
                "error_messages":{
                    "required":"未填写图书名",
                    "min_length":"长度太短了"
                }
            },
            "publish":{
                "write_only":True
            },
            "authors":{
                "write_only":True
            },
            "pic":{
                "read_only":True
            }
        }
    def validate_book_name(self,value):
        if "1" in value:
            raise serializers.ValidationError("包含敏感字")
        request=self.context.get("request")
        print(request)
        return value
    def validate(self, attrs):
        price=attrs.get("price",0)
        if price>999:
            raise serializers.ValidationError("太贵了，没人买得起")
        return attrs