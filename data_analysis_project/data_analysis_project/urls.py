# data_analysis_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('data_analysis_app.urls')),
    path('admin/', admin.site.urls),
    # path('data-analysis/', include('data_analysis_app.urls')),
]