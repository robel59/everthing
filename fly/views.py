from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import base64


@csrf_exempt
def cord_nat(request):
    if request.method == 'POST':
        k = JSONParser().parse(request)
        x = k["x"]
        y = k["y"]
        z = k["z"]
        print("X="+x+"Y="+y+"Z="+z)

        return HttpResponse(status=204)
     