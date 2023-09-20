from django.shortcuts import redirect
from django.urls import reverse
import re
from django.contrib.auth.models import User
from .models import Trainer, Trainee

class WhitelistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        user_type = 5
        try:
            trainer = Trainer.objects.get(user__email = request.user.email)
            user_type = 'Trainer'
        except :
            pass
            # print("not trainer")

        try:
            trainee = Trainee.objects.get(user__email = request.user.email)
            user_type = 'Trainee'
        except:
            pass
            # print("nor trainee")

        
        print(user_type)


        pk = "4"
        match='11'
        match = re.search(r"\/(\d+)\/", request.path)
        if match:
            pk = match.group(1)
        checklist = [
            
            reverse('trainer-create'),
            reverse('trainer-update', args=[pk]),
            reverse('trainer-delete', args=[pk]),
            reverse('trainee-create'),
            reverse('trainee-update', args=[pk]),
            reverse('trainee-delete', args=[pk]),
            reverse('tutorial-create'),
            reverse('tutorial-update', args=[pk]),
            reverse('tutorial-delete', args=[pk]),

        ]
        trainers = [
            reverse('trainee-detail', args=[pk]),
        ]
        trainees = [
            reverse('profile'),
        ]

        if (not request.user.is_authenticated) and ( (request.path in checklist) or (request.path in trainees) or (request.path in trainers) ):
            return redirect('login')

        # # Check if the requested URL is in the whitelist
        if not request.user.is_superuser and request.path in checklist:
            return redirect('login')  # Redirect to login page for unauthorized access

        if not user_type == 'Trainer' and request.path in trainers :
            return redirect('login')
        
        if (user_type == 'Trainee' and request.path in trainees) and not request.user.is_authenticated:
            return redirect('login')

        # Continue with the request if the user is authenticated or the URL is in the whitelist
        response = self.get_response(request)
        return response
