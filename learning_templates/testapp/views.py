from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'text':'Hello world','number':100}
    return render(request,'testapp/index.html',my_dict)

def other(request):
    return render(request,'testapp/other.html')

def relative(request):
    return render(request,'testapp/relative_url_templates.html')
