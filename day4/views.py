from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework import generics
from rest_framework import viewsets

from api.models import Book,Author
from utils.response import APIResponse
from .serializers import BookModelSerializer

class BookAPIView(APIView):
    def get(self,request,*args,**kwargs):
        book_list=Book.objects.filter(is_delete=True)
        data_ser=BookModelSerializer(book_list,many=True).data
        return APIResponse(results=data_ser)

# genericapi
class BookGenericAPIView(ListModelMixin,
                         RetrieveModelMixin,
                         CreateModelMixin,
                         UpdateModelMixin,
                         DestroyModelMixin,
                         GenericAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializer
    lookup_field = "id"
    # 查
    def get(self,request,*args,**kwargs):
        if "id" in kwargs:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)
    # 增
    def post(self,request,*args,**kwargs):
        response=self.create(request,*args,**kwargs)
        return APIResponse(results=response.data)
    # 单改
    def put(self,request,*args,**kwargs):
        response=self.update(request,*args,**kwargs)
        return APIResponse(results=response.data)
    # 局部改
    def patch(self,request,*args,**kwargs):
        response=self.partial_update(request,*args,**kwargs)
        return APIResponse(results=response.data)
    def delete(self,request,*args,**kwargs):
        self.destroy(request,*args,**kwargs)
        return APIResponse(http_status=status.HTTP_204_NO_CONTENT)

class BookListAPIView(generics.ListCreateAPIView,generics.DestroyAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializer
    lookup_field = "id"


class BookGenericViewSet(viewsets.ModelViewSet,CreateModelMixin):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializer
    lookup_field = "id"
    def userlogin(self,request,*args,**kwargs):
        request_data = request.data
        print(request_data)
        book=Book.objects.filter(book_name=request_data.get("book_name"))
        if book:
            print("登陆成功")
            return APIResponse(data_message="登录成功")
        else:
            print(456)
            return APIResponse(data_status=status.HTTP_400_BAD_REQUEST,
                               data_message="登陆失败")
        # return APIResponse(data_message="登录成功")
    def user_count(self,request,*args,**kwargs):
        request_data=request.data
        # print(request_data)
        # return self.list(request,*args,**kwargs)
        # print(self)
        book=Book.objects.all().values("book_name")
        # print(book)
        for i in book:
            # print(i)
            if i.get("book_name")==request_data.get("book_name"):
                return APIResponse(data_message="用户名已存在")
            # else:
        BookGenericAPIView.post(self,request,*args,**kwargs)
        return APIResponse(data_message="注册成功")
        # BookGenericAPIView.post(self,request,*args,**kwargs)
        # return APIResponse(data_message="注册成功")