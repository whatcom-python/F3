from django.http import HttpResponse
def pingfn(request):
    return HttpResponse('Hello LinuxFest!')

