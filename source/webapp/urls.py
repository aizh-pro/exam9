from django.urls import path

from webapp.views import PhotoListView

app_name = 'webapp'

urlpatterns = [
    path('photos', PhotoListView.as_view(), name='index'),
]