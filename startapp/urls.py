from django.urls import path, re_path
from .views import FirebaseView, CreateUserTokenView

app_name='startapp'


urlpatterns = [
    path('create-user/', CreateUserTokenView.as_view()),    
    re_path(r'^firebase/user_id=(?P<user_id>.+)?$', FirebaseView.as_view())

]