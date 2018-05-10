from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import logging
# Create your views here.

# logger = logging.getLogger('django')


@login_required
def index(request):
    return render(request=request, template_name='index.html')
