from django.shortcuts import render

# Create your views here.
def department(request):
    return render(request, 'department.html') 

def flex(request):
    return render(request, 'flex.html')

def layout(request):
    return render(request, 'layout.html')

def table(request):
    return render(request, 'table.html')

def test(request):
    return render(request, 'test.html')
