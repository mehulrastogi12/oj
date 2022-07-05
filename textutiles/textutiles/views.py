# i have created this file-mehul rastogi
from django.http import HttpResponse
from django.shortcuts import render


# code for video 6
# def  index(request):
#           return HttpResponse("<h1>hello hjj</h1>")
# def about(request):
#       return HttpResponse("hey mehul")


def index(request):
    #return HttpResponse("Home")
      params={'name':'harry','place':'mars'}
      return render(request,'index.html',params)
def removepunc(request):
    return HttpResponse("remove punc")
def capfirst(request):
    return HttpResponse("capatalize first")
def newlineremove(request):
    return HttpResponse("newlineremove")
def spaceremove(request):
    return HttpResponse("space remove <a href='/'>back</a>")
def charcount(request):
    return HttpResponse("charcount")

