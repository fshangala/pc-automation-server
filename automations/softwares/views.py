import mimetypes
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Software
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
@login_required
def softwaresView(request):
    template_name="software.html"
    context={}

    softwares=Software.objects.all()
    context["softwares"]=softwares

    return render(request,template_name,context)

@login_required
def download(request,software_id):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = get_object_or_404(Software,pk=software_id)
    # Define the full file path
    filepath = BASE_DIR + "/" + filename.sffile.name
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response