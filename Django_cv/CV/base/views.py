from django.shortcuts import render
from base.models import skills,about

# Create your views here.
def Home(request):
    skils=skills.objects.all()
    About=about.objects.all()
    context={'skils':skils,'About':About}
    return render(request,'base/index.html',context)