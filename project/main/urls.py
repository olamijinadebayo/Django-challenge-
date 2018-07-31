from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='home'),
    url('^list$', views.list, name='list'),
    url('^add$', views.add, name='add'),
]
