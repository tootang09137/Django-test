from django.shortcuts import render

# Create your views here.
def department(request):
    return render(request, 'department.html') 

def flex(request):
    return render(request, 'flex.html')

def index(request):
    return render(request, 'index.html')

def table(request):
    return render(request, 'table.html')

def test(request):
    return render(request, 'test.html')
