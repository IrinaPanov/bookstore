from django.conf.urls import url

from store.views import BookViewSet

urlpatterns = [
    url(r'^bookview/', BookViewSet.as_view(), name='bookview'),
]