from django.http import HttpResponse

def ping(request):
    return HttpResponse("videos app is wired correctly ✅")
