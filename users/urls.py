from django.urls import path
from .views import * 

urlpatterns = [
    path('login/', view=login, name="user-login"),
    path('register/', view=register, name="user-register"),
    path('activate/<int:id>/', view=activate, name="user-activate"),
    path('reset-password/', view=reset_password, name="user-reset-password"),
    path('set-password/<int:id>/', view=set_password, name="user-set-password"),
    path('signout', view=logout, name="user-logout"),
    # Profile links
    path('profile/<int:pk>/', view=ProfileDetailView.as_view(), name="profile-view"),
    path('profile/<int:pk>/edit', view=update_profile, name="profile-edit"),
    path('profile/<int:pk>/delete', view=delete_profile, name="profile-delete")
]