from django.urls import path

from users.views import Detail_user_profile, Update_user_profile

urlpatterns =[
    path('detail-user-profile/<int:pk>/', Detail_user_profile.as_view(), name = 'detail_user_profile'),
    path('update-user-profile/<int:pk>/', Update_user_profile.as_view(), name = 'update_user_profile'),
]