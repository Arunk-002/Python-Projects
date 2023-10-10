from django.shortcuts import render
from base.models import skills,about,carousel,footer

# Create your views here.
def Home(request):
    skils=skills.objects.all()
    About=about.objects.all()
    Carousel=carousel.objects.all()
    Footer=footer.objects.all()
    context={'skils':skils,'About':About,'Carousel':Carousel,'Footer':Footer}
    return render(request,'base/index.html',context)

def Contact(request):
    Footer=footer.objects.all()
    return render(request,'base/contact.html',{'Footer':Footer})
