from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']   else:
    else:
        return render("Login Screen.")    

def logout(request):
    return HttpResponse("Log out Screen.")
    