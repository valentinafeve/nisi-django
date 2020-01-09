from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app_nuser.models import Nisi_user
from app_map.models import Location
from app_network.models import Relation

@csrf_exempt
def near_users(request):
    data = {
        'status':{
            'ok': False,
        },
    }
    body = str(json.loads(json.dumps(request.body.decode('utf8'))))
    body_dct = json.loads(body)
    session_cookie = body_dct["body"]["session_cookie"]
    nuser = Nisi_user.objects.get(token=session_cookie)

    location = Location.objects.get(user=nuser)
    near_users = get_near_users(nuser, location)
    data["near_users"]=near_users
    data["status"]["ok"]=True
    return JsonResponse(data)

@csrf_exempt
def update_location(request):
    data = {
        'status':{
            'ok': False,
        }
    }
    body = str(json.loads(json.dumps(request.body.decode('utf8'))))
    body_dct = json.loads(body)
    position = body_dct["body"]["position"]
    session_cookie = body_dct["body"]["session_cookie"]
    nuser = Nisi_user.objects.get(token=session_cookie)
    city_code=get_city_code(position["lat"], position["lng"])
    location = Location(user=nuser, lng=position["lat"], lat=position["lng"], city_code=city_code)
    location.save()

    data["status"]["ok"] = True
    return JsonResponse(data)

def get_city_code(lat,lng):
    return "BOG"

def get_near_users(actual_nuser, location):
    near_users = Nisi_user.objects.all()
    near_users_json = []
    for nuser in near_users:
        followed = Relation.objects.filter(follower=actual_nuser, follows=nuser).exists()
        near_user_json = {
            "username":str(nuser.user.username),
            # "picture_path":str(nuser.picture_path),
            "picture_path":"https://pbs.twimg.com/profile_images/838851762928791553/Rp1bgpHz_400x400.jpg",
            "rating":str(nuser.rating),
            "followed":followed
        }
        if not actual_nuser.user.username == nuser.user.username:
            near_users_json.append(near_user_json)
    return near_users_json
