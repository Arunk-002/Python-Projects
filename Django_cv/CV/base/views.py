from django.shortcuts import render
from base.models import skills

# Create your views here.
def Home(request):
    skils=skills.objects.all()
    context={skils:'skils'}
    return render(request,'base/index.html',context)