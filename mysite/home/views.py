from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        "variable1":"this is sent",
        "variable2":"deqd"
    }
    #return HttpResponse("this is homepage")
    return render(request,'index.html',context)
def about(request):
    return render(request, 'services.html')
    #return HttpResponse("this is about homepage")
def services(request):

    return HttpResponse("this is service page")
def contact(request):
    return HttpResponse("this is contact page")