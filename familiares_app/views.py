from django.shortcuts import render
from django.http import request
from familiares_app.models import Familiar
# Create your views here.
def home(request):
    queryset = Familiar.objects.all()
    context= {"queryset":queryset}
    return render(request, "index.html", context)