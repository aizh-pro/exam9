from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Photo


class PhotoListView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photos'
    paginate_by = 10

    def get_context_data(self,*, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Photo.objects.all()
        return data.order_by('-created_at')