from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from app_nuser.models import Nisi_user
import json
from .models import Relation

@csrf_exempt
def follow(request):
    data = {
        "status":{
            "ok": False
        }
    }
    body = str(json.loads(json.dumps(request.body.decode('utf8'))))
    body_dct = json.loads(body)
    session_cookie = body_dct["body"]["session_cookie"]
    nuser = Nisi_user.objects.get(token=session_cookie)

    username = body_dct["body"]["user"]["username"]
    user = User.objects.get(username=username)
    follow = Nisi_user.objects.get(user=user)

    if(follow.user.username != nuser.user.username):
        relation = Relation(follower=nuser, follows=follow)
        relation.save()
    else:
        print("What the hell, neighbors algorithm is broken!")

    data["status"]["ok"]=True
    # Authenticated user follows the user with that username
    return JsonResponse(data)

@csrf_exempt
def rate(request):
    # Authenticated user follows the user with that username
    return JsonResponse(data)

@csrf_exempt
def profile(request):
    # Authenticated user follows the user with that username
    return JsonResponse(data)
