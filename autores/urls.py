from autores import views
from django.urls import path

app_name = "autores"
urlpatterns = [
    path("list/", views.AutorListView.as_view(), name="list"),
    path("create/", views.AutorCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.AutorUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.AutorDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", views.AutorDetailView.as_view(), name="detail"),
]
