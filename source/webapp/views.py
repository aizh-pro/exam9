from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import PhotoForm
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


class PhotoView(DetailView):
    template_name = 'photo/photo_view.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PhotoCreateView(CreateView):
    template_name = 'photo/photo_create.html'
    form_class = PhotoForm
    model = Photo

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoUpdateView(UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/photo_update.html'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = reverse_lazy('webapp:index')