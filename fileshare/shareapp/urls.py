from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/',LoginView.as_view(), name='login'),
    path('register/', views.registerView, name="register"),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('sendmail/', views.sendMail, name="sendmail"),
    # path('send_mail_plain',views.SendPlainEmail,name='plain_email'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)