from django.urls import path

from . import views

urlpatterns = [
        path("", views.recent_reads, name = "index"),
        path("user-home", views.user_home, name="user-dash-board"),
        path("user-others/<str:user_name>",views.user_others, name="other-user-page"),
        path("sign-in", views.sign_in, name="sign in"),
        path('sign-out', views.sign_out, name="sign_out"),
        path("sign-up", views.sign_up, name="sign_up"),
        path("delete/<int:id>", views.delete, name="delete"),
        path("api/", views.recently_read_books.as_view(), name="recently-read-books")
]
