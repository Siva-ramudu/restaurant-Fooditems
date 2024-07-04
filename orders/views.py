from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
''' def homepage(request):
    students = [
        {
            'name':'Siva Ram',
            'age' : 22,
            'gender' : 'male',
            'marks' : 75
        },
        {
            'name':'ram',
            'age' : 22,
            'gender':'male',
            'marks' : 34
        },
        {
            'name':'siva',
            'age' : 23,
            'gender':'male',
            'marks' : 90
        }
    ]
    

    
    return render(request,'home.html',{ "students": students }) '''

    
def testpage(request):
    return render(request,'test.html')
