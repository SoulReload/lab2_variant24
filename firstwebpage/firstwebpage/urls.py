from django.contrib import admin
from django.urls import path

from flatpages import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("stage1/", views.initial_text_stage, name="initial_text_stage"),
    path("hello/", views.hello, name="hello"),
    path("hello-plain/", views.hello_plain, name="hello_plain"),
    path("table-stage/", views.table_stage, name="table_stage"),
    path("static-handler/", views.static_handler, name="static_handler"),
]
