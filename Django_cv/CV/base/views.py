from django.shortcuts import render,redirect
from base.models import skills,about,carousel,footer
from base.forms import contactform
from django.contrib import messages

# Create your views here.
def Home(request):
    skils=skills.objects.all()
    About=about.objects.all()
    Carousel=carousel.objects.all()
    Footer=footer.objects.all()
    context={'skils':skils,'About':About,'Carousel':Carousel,'Footer':Footer}
    return render(request,'base/index.html',context)

def Contact(request):
    form=contactform()
    Footer=footer.objects.all()
    
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Message is Successfully Sent")
            return redirect('home')


    context={'Footer':Footer,'form':form}
    return render(request,'base/contact.html',context)
