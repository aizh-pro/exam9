from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import View

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


class PhotoCreateView(PermissionRequiredMixin,CreateView):
    template_name = 'photo/photo_create.html'
    form_class = PhotoForm
    model = Photo
    permission_required = 'webapp.photo_create'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoUpdateView(PermissionRequiredMixin,UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/photo_update.html'
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin,DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    permission_required = 'webapp.change_photo'
    success_url = reverse_lazy('webapp:index')

    def has_permission(self):
        photo = self.get_object()
        return super().has_permission() or photo.author == self.request.user


class PhotoAddFavoritesView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        if request.user not in photo.who_likes.all():
            photo.who_likes.add(request.user)
            print("DEBUG")
            print(photo)
            photo.save()
            return HttpResponse({'message': "Added"})
        else:
            return HttpResponseForbidden()


class PhotoRemoveFavoritesView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        if request.user in photo.who_likes.all():
            photo.who_likes.remove(request.user)
            print("DEBUG")
            print(photo)
            photo.save()
            return HttpResponse({'message': "Removed"})
        else:
            return HttpResponseForbidden()