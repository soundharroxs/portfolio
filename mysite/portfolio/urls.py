from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("Homepage",views.portfolio,name="portfolio")
]
urlpatterns += staticfiles_urlpatterns()