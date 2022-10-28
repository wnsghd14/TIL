
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model






class  CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','usertall','userweights','userfat','user_sm']


class  CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = "__all__"