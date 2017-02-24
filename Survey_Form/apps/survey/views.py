from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"survey/index.html")

def show(request):
    # request.session['name'] = request.POST['first_name']
    context = {
        'name':request.POST['name'],
        'location':request.POST['location'],
        'language':request.POST['language'],
        'comment':request.POST['comment'],
    }
    print(request.method)

    return render(request,"survey/show.html",context)

def create(request):
    print (request.method)
    if request.method == "POST":
        print('*'*50)
        print (request.POST)
        print('*'*50)
    else:
        return redirect('survey/show.html')
