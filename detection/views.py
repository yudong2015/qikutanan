#encoding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
from models import *


@csrf_exempt
def wechat_url(request):
    if request.method == 'GET':
        echostr = request.GET.get('echostr','')
        return HttpResponse(echostr)

#@require_http_methods(['POST'])
@csrf_exempt
def reward(request):
    user = request.user
    if not user:
        return JsonResponseRedirect({'message':'user is not authed!'},status=400)
    if DrawRecord.objects.filter(user=user).exists():
        return JsonResponse({'message':'you have drawed!'},status=400)
    data = json.loads(request.body)
    time = data.get('time','')

    try:
        time = float(time)
       # time = float(0.5)
    except:
        return JsonResponse({'message':'param is error!'},status=400)
    if time == 0.5: #电影票或周边
        if Reward.objects.filter(type='movieTicket',remain__gt=0).exists():
            reward_type = 'movieTicket'
        elif Reward.objects.filter(type='movieArround',remain__gt=0).exists():
            reward_type = 'movieArround'
        elif Reward.objects.filter(type='vipshopTicket',remain__gt=0).exists():
            reward_type = 'vipshopTicket'
        else:
            reward_type = 'qikuBag'

    elif time < 0.4 or time > 0.6: #奇酷大礼包
        reward_type = 'qikuBag'
    else: #唯品会券
        reward_type = 'vipshopTicket' if Reward.objects.filter(type='vipshopTicket',remain__gt=0).exists() else 'qikuBag'

    if reward_type == 'qikuBag':
        reward = Reward.objects.filter(type=reward_type, remain__gt=0)[0]
        DrawRecord.objects.create(user=user,reward=reward)
    elif reward_type == 'vipshopTicket':
        reward = Reward.objects.filter(type=reward_type, remain__gt=0)[0]
        reward.remain = reward.remain - 1
        reward.save()
        DrawRecord.objects.create(user=user,reward=reward)
    else:
        name = data.get('name','')
        phone = data.get('phone','')
        address = data.get('address','')
        name = ''
        phone = 'phone'
        address = 'address'
        if name and phone and address:
            Person.objects.create(user=user,name=name,phone=phone,address=address)
            reward = Reward.objects.filter(type=reward_type, remain__gt=0)[0]
            reward.remain = reward.remain - 1
            reward.save()
            DrawRecord.objects.create(user=user,reward=reward)
        
    return JsonResponse({'reward':reward_type},status=200)


@csrf_exempt
def accounts_profile(request):
    return drawed(request)


@csrf_exempt
def drawed(request):
    user = request.user
    if not user:
       return HttpResponseRedirect('/login/')
    try:
        if DrawRecord.objects.filter(user=user).exists():
            reward = DrawRecord.objects.get(user=user).reward.type
            return JsonResponse({'drawed':1,'reward':reward},status=200)
        else:
            return JsonResponse({'drawed':0},status=200)
    except:
        return JsonResponse({'message':'Server Internal Error'},status=500)


