from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def hello(request, name):
    return HttpResponse("Hello, " + str(name))

def home(request):
    return render(request,"index.html")

def process(request):
    if request.method == "POST":
        request.session["pizza_kind"] = request.POST["kind"]
        request.session["pizza_size"] = request.POST["size"]
        request.session["pizza_boxes"] = request.POST["boxes"]
        return redirect("/display")
    
def display(request):
    return render(request, "display.html")
        
