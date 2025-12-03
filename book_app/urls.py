from django.urls import path

from . import views

urlpatterns = [
        path("", views.index, name = "index"),
        path("recent-reads", views.recent_reads, name="recently read books"),
        path("user-others/<str:user_name>",views.user_others, name="other-user-page"),
        path("sign-in", views.sign_in, name="sign in"),
        path('sign-out', views.sign_out, name="sign_out")
]
