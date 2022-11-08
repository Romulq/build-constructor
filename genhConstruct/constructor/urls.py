from django.urls import path, include

from .views import MainView, BuildView, ProfileView, LoginView, LogoutView
from .api import urls

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('build/<slug:slug>/', BuildView.as_view(), name='build'),

    path('profile/', ProfileView.as_view(), name='profile'),

    path('login/', LoginView.as_view(), name="sign_in"),
    path('logout/', LogoutView.as_view(), name="sign_out"),
    # path('registration/', RegistrationView.as_view(), name="sign_up"),

    path('api/v1/', include(urls.urlpatterns)),
    path('api-auth/', include('rest_framework.urls')),
]
