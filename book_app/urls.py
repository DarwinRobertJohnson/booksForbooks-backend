from django.urls import path

from . import views

urlpatterns = [
        path("", views.index, name = "index"),
        path("recent-reads", views.recent_reads, name="recently read books")
]
