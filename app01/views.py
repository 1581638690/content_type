from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def test(request):
    # PricePolicy.objects.create(
    #     valid_period=7,
    #     price=6.6,
    #     content_type=ContentType.objects.get(model="Course"),#查询到课程表 存入
    #     object_id=1
    #
    # )
    # PricePolicy.objects.create(
    #     valid_period=14,
    #     price=9.9,
    #     content_object=Course.objects.get(id=2)
    # )

    #根据某个价格策略对象，找到他对应的表和数据，如：管理课程名称
    # price=PricePolicy.objects.get(id=2)
    # print(price.content_object.name)


    #找到某个课程关联的所有价格册罗
    obj=Course.objects.get(id=1)#获取到21天学python
    for obj in obj.policy_list.all():
        print(obj.price)
    return render(request,"index.html")