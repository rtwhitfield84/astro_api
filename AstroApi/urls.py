"""AstroApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api.views import user_view, tab_view, register_view, logout_view

router = routers.DefaultRouter()
router.register(r'users', user_view.UserViewSet)
router.register(r'tabs', tab_view.TabViewSet, base_name='tabs')

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include(router.urls)),
	url(r'^api-token-auth/', obtain_auth_token),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^register', register_view.RegisterView.as_view()),
	# url(r'^register', user_view.RegisterView.as_view()),
	url(r'^logout/', logout_view.Logout.as_view()),
]
