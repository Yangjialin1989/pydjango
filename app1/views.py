from django.shortcuts import render, HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
# 函数默认需要request参数
def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    return HttpResponse('用户列表')


def user_add(request):
    # 默认情况django会在当前app下templates目录下照
    return render(request, 'user_add.html')

def news(request):
    # 请求
    # pip install requests
    # 导入
    res = requests.get("https://mbdp01.bdstatic.com/static/landing-pc/css/news.58e76a98.css")
    data_list = res.json()
    print(data_list)
    return render(request, 'news.html')


def template(request):
    #
    name = '韩非子'
    roles = ['js', 'html', 'css']
    user_info ={'name':'郭美美','salary':100000,'role':'CEO'}
    return render(request, 'template.html',
                  {
                      'n1': name,
                      'n2': roles,
                      'n3':user_info
                  })
