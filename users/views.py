from users.models import UserProfile

from django.urls import reverse

from django.views.generic import DetailView, UpdateView

class Detail_user_profile(DetailView):
    model = UserProfile
    template_name= 'users/detail_user_profile.html'

class Update_user_profile(UpdateView):
    model = UserProfile
    template_name = 'users/update_user_profile.html'
    fields = ['phone', 'profile_image']

    def get_success_url(self):
        return reverse('detail_user_profile', kwargs = {'pk':self.object.pk})