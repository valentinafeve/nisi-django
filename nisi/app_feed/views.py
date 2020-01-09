from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app_network.models import Relation
import json
from app_nuser.models import Nisi_user, SN

@csrf_exempt
def tw_followings(request):
    body = str(json.loads(json.dumps(request.body.decode('utf8'))))
    body_dct = json.loads(body)
    session_cookie = body_dct["body"]["session_cookie"]
    nuser = Nisi_user.objects.get(token=session_cookie)
    followings = Relation.objects.filter(follower=nuser)
    tw_followings = []
    print(followings)
    for following in followings:
        print(following)
        sn = SN.objects.filter(user=following.follows, name='tw')
        if(sn.exists()):
            tw_followings.append(sn[0].username)
    data = {'twitter':{'users': tw_followings}}
    print("User:")
    print(request.user)
    return JsonResponse(data)

@csrf_exempt
def fb_followings(request):
    users = ['Nessnio','NoticiasUno','SaninPazC','dw_learngerman','elespectador', 'BluRadioCo', 'petrogustavo']
    data = {'facebook':{'users': users}}
    return JsonResponse(data)

@csrf_exempt
def ig_followings(request):
    users = ['oceans.orcas']
    data = {'instagram':{'users': users}}
    return JsonResponse(data)

@csrf_exempt
def notifications(request):
    # Authenticated user follows the user with that username
    return JsonResponse(data)
