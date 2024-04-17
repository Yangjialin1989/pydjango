from django.shortcuts import render,HttpResponse
from django.shortcuts import render

# Create your views here.
# 函数默认需要request参数
def index(request):
    return HttpResponse('欢迎使用')







