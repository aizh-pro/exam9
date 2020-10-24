from django.urls import path, include

from webapp.views import PhotoListView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, \
    PhotoAddFavoritesView

app_name = 'webapp'

# urlpatterns = [
#     path('photos', PhotoListView.as_view(), name='index'),
#     path('photos', PhotoView.as_view(), name='photo_view'),
# ]

urlpatterns = [
    path('', PhotoListView.as_view(), name='index'),

    path('photos/', include([
        path('add/', PhotoCreateView.as_view(), name='photo_create'),
        path('<int:pk>/', include([
            path('', PhotoView.as_view(), name='photo_view'),
            path('update/', PhotoUpdateView.as_view(), name='photo_update'),
            path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
            # path('add-to-cart/', CartAddView.as_view(), name='product_add_to_cart'),
            path('like/', PhotoAddFavoritesView.as_view(), name='photo_like'),
            # path('unlike/', ArticleUnLikeView.as_view(), name='article_unlike'),
        ])),
    ])),
]
