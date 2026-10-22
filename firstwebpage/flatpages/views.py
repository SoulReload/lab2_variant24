from django.http import HttpResponse
from django.shortcuts import render


def initial_text_stage(request):
    """Preserve the first exercise stage: root originally returned plain text."""
    return HttpResponse("Привет, Мир!", content_type="text/plain; charset=utf-8")


def hello(request):
    """The /hello/ route returns the same explicitly plain-text greeting."""
    return HttpResponse("Привет, Мир!", content_type="text/plain; charset=utf-8")


def hello_plain(request):
    """Same greeting without content_type; Django uses its default text/html."""
    return HttpResponse("Привет, Мир!")


def home(request):
    """Final root view after the template section: financial index page."""
    return render(request, "index.html")


def table_stage(request):
    """Expanded table before the separate CSS/static-files exercise."""
    return render(request, "table_stage.html")


def static_handler(request):
    """Final styled copy of the expanded financial-reporting template."""
    return render(request, "static_handler.html")
