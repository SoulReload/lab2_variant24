from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Final home page after the template section: the original green 4x5 table."""
    return render(request, "index.html")


def initial_text_stage(request):
    """Preserve the first step, when the root view returned plain text."""
    return HttpResponse("Привет, Мир!", content_type="text/plain; charset=utf-8")


def hello(request):
    """Return the same greeting with an explicit plain-text content type."""
    return HttpResponse("Привет, Мир!", content_type="text/plain; charset=utf-8")


def hello_plain(request):
    """Return the greeting without content_type; Django uses its default."""
    return HttpResponse("Привет, Мир!")


def table_stage(request):
    """Show the stage after the table/list-heading tasks, before external CSS."""
    return render(request, "table_stage.html")


def static_handler(request):
    """Show the later edited copy with the CSS and local image."""
    return render(request, "static_handler.html")
