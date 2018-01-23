from django.conf.urls import url, include
from django.contrib import admin
from textClassification import views
urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^sentiment/', include('textClassification.urls')),
    url(r'^', view=views.index),

]
