# data_analysis_app/urls.py
from django.urls import path
from .views import data_tab, descriptive_statistics_tab, exploratory_data_analysis_tab, profile_view, export_to_csv,predict_survival, export_to_excel, index

urlpatterns = [
    path('', index, name='index'), #To load cover.html when an empty URL is passed
    path('data/', data_tab, name='data_tab'),
    path('descriptive-statistics/', descriptive_statistics_tab, name='descriptive_statistics_tab'),
    path('exploratory-data-analysis/', exploratory_data_analysis_tab, name='exploratory_data_analysis_tab'),
    path('profile/', profile_view, name='profile_view'),
    path('survival-prediction/', predict_survival, name='predict_survival'),
    path('export/csv/', export_to_csv, name='export_to_csv'),
    path('export/excel/', export_to_excel, name='export_to_excel'),
]