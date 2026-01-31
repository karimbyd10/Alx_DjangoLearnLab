from django.http import HttpResponse

def secure_view(request):
    response = HttpResponse("Secure Content")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response

