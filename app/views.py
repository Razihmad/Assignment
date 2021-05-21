from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Marks
# Create your views here.
def home(request):
    return render(request,'home.html')


def marks(request):
    if request.method == 'POST':
        rollnumber = request.POST.get('roll')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        math = float(request.POST.get('maths'))
        physics = float(request.POST.get('physics'))
        chemistry = float(request.POST.get('chemistry'))
        total = float(request.POST.get('total'))
        percentage = round(float(request.POST.get('percentage')),3)
        if Marks.objects.filter(RollNumber=rollnumber):
            messages.info(request,"This Student Has Already Been Added")
            return redirect('marks')
        else:
            if not (first_name.isalpha() and last_name.isalpha() and rollnumber.isalnum()):
                messages.info(request,"Please Enter A Valid Name")
                return redirect('marks')
            
            marks = Marks(RollNumber = rollnumber,first_name = first_name,last_name=last_name,Maths = math,Physics=physics,Chemistry=chemistry,Total = total,Percentage = percentage)
            marks.save()
            messages.success(request,"Marks has Been Added successfully")
            return redirect("leaderboard")

    return render(request,'marks.html')

def leaderboard(request):
    l = list(Marks.objects.order_by('Percentage')[::-1])
    ind = [i for i in range(1,len(l) +1 )]
    data = list(zip(l,ind)) 
    return render(request, 'leaderboard.html',{'data':data})
    