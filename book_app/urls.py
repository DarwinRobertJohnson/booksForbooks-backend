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
        path("api/", views.recently_read_books.as_view(), name="recently-read-books"),
        path("api/accounts/signin",views.api_login, name="sign in api"),
        path("api/users/<str:user_name>",views.user_others_api, name="other-user-api"),
        path("api/dashboard",views.user_dashboard_api, name="user-dashboard-api"),
        path("api/users/actions/delete/<int:id>",views.user_action_delete, name="user action delete api"),
        path("api/users/actions/add/",views.user_action_add, name="user action add api"),
        path("api/accounts/signup", views.api_signup, name="user action create account"),
        path("api/accounts/logout", views.api_logout, name="user action logout"),
        path("api/users/actions/toggle", views.user_action_toggle, name="toggle book status")
]
