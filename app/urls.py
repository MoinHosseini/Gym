from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from .views import(
    home,about,blog,contact,service,SignUp,anatomy,

    TutorialListView, TutorialDetailView, TutorialCreateView, TutorialUpdateView, TutorialDeleteView,

    TrainerListView, TrainerDetailView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView,

    TraineeListView, TraineeDetailView, TraineeCreateView, TraineeUpdateView, TraineeDeleteView,

    tutorials_with_muscle_name,profile,



)
urlpatterns = [
    path('', home , name="home" ),
    path('about/', about , name="about" ),
    path('blog/', blog , name="blog" ),
    path('contact/', contact , name="contact" ),
    path('service/', service , name="service" ),
    path('signup/', SignUp.as_view() , name="sign-up" ),

    path('anatomy/', anatomy , name="anatomy" ),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),

    path('trainers/', TrainerListView.as_view(), name='trainer-list'),
    path('trainers/<int:pk>/', TrainerDetailView.as_view(), name='trainer-detail'),
    path('trainers/create/', TrainerCreateView.as_view(), name='trainer-create'),
    path('trainers/<int:pk>/update/', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainers/<int:pk>/delete/', TrainerDeleteView.as_view(), name='trainer-delete'),


    path('trainees/', TraineeListView.as_view(), name='trainee-list'),
    path('trainees/<int:pk>/', TraineeDetailView.as_view(), name='trainee-detail'),
    path('trainees/create/', TraineeCreateView.as_view(), name='trainee-create'),
    path('trainees/<int:pk>/update/', TraineeUpdateView.as_view(), name='trainee-update'),
    path('trainees/<int:pk>/delete/', TraineeDeleteView.as_view(), name='trainee-delete'),

    path('tutorial/', TutorialListView.as_view(), name='tutorial-list'),
    path('tutorial/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail'),
    path('tutorial/create/', TutorialCreateView.as_view(), name='tutorial-create'),
    path('tutorial/<int:pk>/update/', TutorialUpdateView.as_view(), name='tutorial-update'),
    path('tutorial/<int:pk>/delete/', TutorialDeleteView.as_view(), name='tutorial-delete'),

    path('tutorial/<str:muscle_name>/',tutorials_with_muscle_name , name='tutorial-anatomy'),
    path('profile/',profile , name='profile'),

]