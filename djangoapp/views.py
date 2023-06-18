from django.shortcuts import render, redirect

from djangoapp.forms import PersonForm
from djangoapp.models import Person


# Create your views here.

def index(request):
    if request.method == "POST":
        form = PersonForm(data=request.POST)
        if form.is_valid():
            form.save()
        # return redirect("index")
    people = Person.objects.all()
    context = {
        'people': people,
        'form': PersonForm
    }

    return render(request, "index.html", context=context)
