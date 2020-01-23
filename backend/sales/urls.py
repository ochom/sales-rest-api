from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('', views.index, name="sales api index"),

    path('agents/', views.Agents.as_view()),
    path('agent/<int:pk>', views.AgentDetail.as_view()),

    # path('agent/skills/', views.Agents.as_view()),  # retrive agent skills with agent id provides as a request parameter
    # path('skills/agent/<int:pk>', views.AgentDetail.as_view()), #  create skill for agent of pk

    path('clients/', views.Clients.as_view()),
    path('client/<int:pk>', views.ClientDetail.as_view()),

    path('orders/', views.Orders.as_view()),
    path('order/<int:pk>', views.OrderDetail.as_view()),

    path('products/', views.Products.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
