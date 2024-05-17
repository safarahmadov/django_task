from django.shortcuts import render

# Create your views here.
def main(request):
    if request.method == "POST":
        text = request.POST["text"]
        text_get=text.split()
        if len(text_get)<=1:
            context = { "text":f"{len(text)} herf"}
            return render(request, "main.html", context)
        else: 
            context= {"text":f"{len(text_get)} soz"}  
            return render(request, "main.html", context )