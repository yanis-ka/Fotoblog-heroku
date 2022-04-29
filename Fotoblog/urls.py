from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
import authentication.views
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('signup/', authentication.views.SignUpPageView.as_view(), name='signup'),
    path('login/', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(
        template_name='authentication/logged_out.html'),
        name='logout'),
    # path('password_change/', PasswordChangeView.as_view(
    #     template_name = 'authentication/password_change_form.html',
    #     success_url = 'password_change_done',
    #     ), 
    #     name='password_change'),
    # path('password_change/password_change_done/', PasswordChangeDoneView.as_view(
    #     template_name = 'authentication/password_change_done.html'
    #     ),
    #     name='change_success'),
    # path('profile-photo/upload', authentication.views.UploadProfilePhotoView.as_view(),
    #     name='upload_profile_photo'),
]
