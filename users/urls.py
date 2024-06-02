
from django.urls import path


from users import views

app_name="users"

urlpatterns = [
    path('reg/', views.registry, name='registry'),

]
