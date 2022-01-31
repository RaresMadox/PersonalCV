from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    # path('signup/',views.signup_view,name="signup"),
    # path('login/',views.login_view,name="login"),
    # path('logout/',views.logout_view,name="logout")
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('user/',views.userPage,name="userpage"),


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_confirm.html") ,name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_complete.html"),name="password_reset_complete"),
]


