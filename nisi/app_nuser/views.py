from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse

import hashlib

from app_nuser.models import Nisi_user, SN

import json
import datetime

@csrf_exempt
def signup(request):
    data = {
        'status':{
            'ok': False,
        },
        'session':{
            'token':'',
        }
    }
    if request.method == 'POST':
        body = str(json.loads(json.dumps(request.body.decode('utf8'))))
        body_dct = json.loads(body)
        username = body_dct["body"]["username"]
        password = body_dct["body"]["password"]
        phone = body_dct["body"]["phone"]
        print("%s is trying to sign up" % username)
        user = None
        try:
            user = User.objects.create_user(username, "email@email.com", password)
            user.save()
            nisi_user = Nisi_user(user=user, phone=phone)
            nisi_user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                to_hash = username+str(datetime.datetime.now())
                token = hashlib.sha224(to_hash.encode()).hexdigest()
                data["status"]["ok"] = True;
                data["session"]["token"]=token
                nuser = Nisi_user.objects.get(user=user)
                nuser.token = token
                nuser.save()
        except:
            if user is not None:
                user.delete()
        data["status"]["ok"]=True
    return JsonResponse(data)

@csrf_exempt
def signin(request):
    data = {
        'status':{
            'ok': False
        },
        'session':{
            'token':''
        },
        # User wasn't found
        'response':0
    }
    try:
        print(request.method)
        if request.method == 'POST':
            body = str(json.loads(json.dumps(request.body.decode('utf8'))))
            body_dct = json.loads(body)
            username = body_dct["body"]["username"]
            password = body_dct["body"]["password"]
            print("%s is trying to sign in " % username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                to_hash = username+str(datetime.datetime.now())
                token = hashlib.sha224(to_hash.encode()).hexdigest()
                nuser = Nisi_user.objects.get(user_id=user.id)
                nuser.token = token
                nuser.save()
                data["session"]["token"]=token
                data["response"]=1
            else:
                data["response"]=2
            data["status"]["ok"] = True;
    except:
        data["status"]["ok"] = False;
    return JsonResponse(data)

@csrf_exempt
def profile(request):
    data = {
        'status':{
            'ok':True
        }
    }

    body = str(json.loads(json.dumps(request.body.decode('utf8'))))
    body_dct = json.loads(body)
    session_cookie = body_dct["body"]["session_cookie"]
    nuser = Nisi_user.objects.get(token=session_cookie)
    tg, ig, fb, tw = get_sns(nuser)
    profile = {
        "username":nuser.user.username,
        "first_name": nuser.first_name,
        "last_name": nuser.last_name,
        "rating": nuser.rating,
        "picture_path": nuser.picture_path,
        "about": nuser.about,
        "email": nuser.email,
        "phone": nuser.phone,
        "born_date": nuser.born_date,
        "irated": 23,
        "ratedme": 2009,
        "sns": {
          "telegram": tg,
          "instagram": ig,
          "facebook": fb,
          "twitter": tw
        }
    }
    data["profile"] = profile
    return JsonResponse(data)

@csrf_exempt
def settings(request):
    # Authenticated user follows the user with that username
    return JsonResponse(data)

@csrf_exempt
def update_setting(request):
    # Authenticated user follows the user with that username
    return JsonResponse(data)

def get_sns(user):
    tg, ig, fb, tw = ('', '', '', '')
    tg_temp = SN.objects.filter(user=user, name="tg")
    if tg_temp:
        tg_temp=tg_temp[0]
        tg = {
            "username":tg_temp.username,
            "verified":tg_temp.verified,
        }
    ig_temp = SN.objects.filter(user=user, name="ig")
    if ig_temp:
        ig_temp=ig_temp[0]
        ig = {
            "username":ig_temp.username,
            "verified":ig_temp.verified,
        }
    fb_temp = SN.objects.filter(user=user, name="fb")
    if fb_temp:
        fb_temp = fb_temp[0]
        fb = {
            "username":fb_temp.username,
            "verified":fb_temp.verified,
        }

    tw_temp = SN.objects.filter(user=user, name="tw")
    if tw_temp:
        tw_temp = tw_temp[0]
        tw = {
            "username":tw_temp.username,
            "verified":tw_temp.verified,
        }
    return (tg, ig, fb, tw)

@csrf_exempt
def add_sn(request):
    data = {
        "status":{
            "ok": False
        },
    }
    body = str(json.loads(json.dumps(request.body.decode('utf8'))))
    body_dct = json.loads(body)
    session_cookie = body_dct["body"]["session_cookie"]
    type = body_dct["body"]["session_cookie"]
    sn = body_dct["body"]["sn"]
    sn_name = sn["name"]
    sn_username = sn["username"]
    nuser = Nisi_user.objects.get(token=session_cookie)
    sn = None
    try:
        sn = SN.objects.filter(user=nuser, name=sn_name)[0]
        sn.username = sn_username;
        sn.save()
    except:
        sn = SN(
            user=nuser,
            code='',
            name=sn_name,
            username=sn_username,
            verified=False,
            )
        sn.save()
    data["status"]["ok"]=True
    return JsonResponse(data)
