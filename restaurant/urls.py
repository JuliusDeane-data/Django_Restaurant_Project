from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("order/<int:pk>/", login_required(views.OrderView.as_view()), name="order"),
    path("details/", login_required(views.DetailsView.as_view()), name="details"),
    path("login/", views.CustomLoginView.as_view(), name='login'),
    path("logout/", views.logoutUser, name='logout'),

]