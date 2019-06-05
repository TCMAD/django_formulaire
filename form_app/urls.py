from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.Acceuil.as_view(),name="acceuil"),
    path('detail/<int:id>/',views.detail,name="detail"),
    # path('detail/<int:pk>/',views.FormDetailView.as_view(),name="detail"),
    path('search/',views.search,name="search"),
    path('forms/create',views.FormCreateView.as_view(),name="create"),
    path('forms/update/<int:pk>',views.FormUpdateView.as_view(),name="update"),
    path('forms/delete/<int:pk>',views.FormDeleteView.as_view(),name="delete"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
 ]
