from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    Search,
    first, second, third, fourth, fivth, sixth, other
)

app_name = "articles"

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("search/", Search.as_view(), name="search"),
    path("first/", first, name="first"),
    path("second/", second, name="second"),
    path("third/", third, name="third"),
    path("fourth/", fourth, name="fourth"),
    path("fivth/", fivth, name="fivth"),
    path("sixth/", sixth, name="sixth"),
    path("other/", other, name="other"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ArticleDeleteView.as_view(), name="delete"),
]
