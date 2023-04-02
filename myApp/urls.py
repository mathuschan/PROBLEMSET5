from django.urls import path
from . import views

# a namespace for our app, this will become important in the Templates section
app_name = 'myApp'

# we call the path function to let Django know what of our Python function should be
# called when a certain URL has been entered.
# The name parameter is optional, but lets us later more conveniently link between pages.
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_element, name='add_joke'),
    path('delete_all/', views.delete_all, name='delete_all'),
]