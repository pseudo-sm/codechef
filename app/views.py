from django.shortcuts import render
from django.http import JsonResponse
import requests
from . models import Submissions
# Create your views here.

def editor(request):

    return render(request,"editor.html")


url = "https://api.hackerearth.com/v3/code/compile/"
run_url = "https://api.hackerearth.com/v3/code/run/"


def gfg_compile(lang, code, _input=None, save=False):
    data = {
      'lang': lang,
      'source': code,
      "client_secret" : "9e94c82bb37aad13733fa9815ab23bfe522b6520",
      "input" : _input
    }

    r = requests.post(url,data=data)
    r = requests.post(run_url,data=data)
    return r

def compile(request):

    lang = request.GET.get("lang")
    code = request.GET.get("code")
    input = request.GET.get("input")
    result = gfg_compile(lang,code,input)
    print(result.json())
    return JsonResponse({"output" : result.json()},safe=False)


def editor(request):

    return render(request,"editor.html")




def start_exam(request):
    rn = request.GET.get("rn")
    name = request.GET.get("name")
    dish = request.GET.get("dish")
    request.session["rn"] = rn
    request.session["name"] = name
    request.session["starter"] = dish
    return JsonResponse(True,safe=False)

def start_exam2(request):
    dish = request.GET.get("dish")
    request.session["main"] = dish
    return JsonResponse(True,safe=False)


def start_exam3(request):
    dish = request.GET.get("dish")
    request.session["desert"] = dish
    return JsonResponse(True,safe=False)

def submit1(request):

    name = request.session["name"]
    dish = request.session["dish"]
    code = request.GET.get("code")
    submission = Submissions.objects.create(name=name,starter=code,dish_starter=dish)
    request.session["submission"] = submission.pk
    return JsonResponse(submission.pk,safe=False)

def submit2(request):

    code = request.GET.get("code")
    submission = Submissions.objects.get(pk=request.session["submission"])
    submission.dish_main = request.session["main"]
    submission.main = code
    submission.save()
    return JsonResponse(submission.pk,safe=False)

def submit3(request):

    code = request.GET.get("code")
    submission = Submissions.objects.get(pk=request.session["submission"])
    submission.dish_desert = request.session["desert"]
    submission.desert = code
    submission.save()
    return JsonResponse(submission.pk,safe=False)

def editor2(request):

    return render(request,"editor2.html")

def editor3(request):

    return render(request,"editor3.html")
