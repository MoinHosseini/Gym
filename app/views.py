from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/about-us.html")

def blog(request):
    return render(request, "app/blog.html")

def contact(request):
    return render(request, "app/contact-us.html")

def service(request):
    return render(request, "app/services.html")

def anatomy(request):
    return render(request, "anatomy.html")


from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUp(generic.CreateView):
    
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "user/user_form.html"


from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Trainee, Trainer
from django.http import HttpResponseRedirect

class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee/trainee_list.html'  # Replace with your template name
    context_object_name = 'trainees'


class TraineeDetailView(DetailView):
    model = Trainee
    template_name = 'trainee/trainee_detail.html'
    context_object_name = 'trainee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add tutorials to the context
        context['tutorials'] = Tutorial.objects.all()
        # trainee = self.get_object()
        # workout_schedule = trainee.workout_schedule.values()
        # l = []
        # for item in workout_schedule:
        #     l.append(item)
        # context['workout_schedule'] = l

        return context

    def post(self, request, *args, **kwargs):
        # Check if the form was submitted
        tutorial_id = request.POST.get('tutorial_id')
        selected_tutorial = Tutorial.objects.get(pk=tutorial_id)
        trainee = self.get_object()  # Access the trainee instance using self.get_object()

        if str(tutorial_id) in trainee.workout_schedule.keys():
            del trainee.workout_schedule[str(tutorial_id)]
        else:
            # Like the book
            trainee.workout_schedule[tutorial_id] = selected_tutorial.name

        trainee.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))







class TraineeCreateView(CreateView):
    model = Trainee
    template_name = 'trainee/trainee_form.html'  # Replace with your template name
    fields = '__all__'
    success_url = reverse_lazy('trainee-list')

class TraineeUpdateView(UpdateView):
    model = Trainee
    template_name = 'trainee/trainee_form.html'  # Replace with your template name
    fields = '__all__'
    success_url = reverse_lazy('trainee-list')

class TraineeDeleteView(DeleteView):
    model = Trainee
    template_name = 'ttrainee/rainee_confirm_delete.html'  # Replace with your template name
    success_url = reverse_lazy('trainee-list')




class TrainerListView(ListView):
    model = Trainer
    template_name = 'trainer/trainer_list.html'  # Replace with your template name
    context_object_name = 'trainers'

class TrainerDetailView(DetailView):
    model = Trainer
    template_name = 'trainer/trainer_detail.html'  # Replace with your template name
    context_object_name = 'trainer'

class TrainerCreateView(CreateView):
    model = Trainer
    template_name = 'trainer/trainer_form.html'  # Replace with your template name
    fields = '__all__'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    template_name = 'trainer/trainer_form.html'  # Replace with your template name
    fields = '__all__'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer/trainer_confirm_delete.html'  # Replace with your template name
    success_url = reverse_lazy('trainer-list')



from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tutorial

class TutorialListView(ListView):
    model = Tutorial
    template_name = 'tutorial/tutorial_list.html'  # Replace with your template name
    context_object_name = 'tutorials'

class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = 'tutorial/tutorial_detail.html'  # Replace with your template name
    context_object_name = 'tutorial'

class TutorialCreateView(CreateView):
    model = Tutorial
    template_name = 'tutorial/tutorial_form.html'  # Replace with your template name
    fields = '__all__'
    success_url = reverse_lazy('tutorial-list')

class TutorialUpdateView(UpdateView):
    model = Tutorial
    template_name = 'tutorial/tutorial_form.html'  # Replace with your template name
    fields = '__all__'
    success_url = reverse_lazy('tutorial-list')

class TutorialDeleteView(DeleteView):
    model = Tutorial
    template_name = 'tutorial/tutorial_confirm_delete.html'  # Replace with your template name
    success_url = reverse_lazy('tutorial-list')



def tutorials_with_muscle_name(request,muscle_name):
    
    tutorials = Tutorial.objects.filter(muscle_name=muscle_name)

    context = {
        'tutorials': tutorials,
        'muscle_name' : muscle_name,
    }

    return render(request, 'tutorial/tutorial_list_with_muscle.html', context)



def profile(request):
    trainee = Trainee.objects.get(user__email = request.user.email)
    return render(request, "user/profile.html", {"trainee":trainee})

