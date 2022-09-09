from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from . import models


def index(request):
    return render(request, "index.html")


def media(request, pk):
    user = request.user
    if user.is_anonymous:
        raise Http404()
    file = get_object_or_404(models.SomeFile, pk=pk)
    response = HttpResponse()
    response["Content-Disposition"] = f"attachment; filename={file.basename()}"
    response["X-Accel-Redirect"] = f"/protected/{file.file.name}"
    return response
