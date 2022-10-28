from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "usertall", "userweights", "userfat", "user_sm", "gender"]
        labels = {
            "usertall": "키",
            "userweights": "몸무게",
            "userfat": "체지방량",
            "user_sm": "골격근량",
            "gender": "성별",
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "usertall", "userweights", "userfat", "user_sm", "gender"]
        labels = {
            "usertall": "키",
            "userweights": "몸무게",
            "userfat": "체지방량",
            "user_sm": "골격근량",
            "gender": "성별",
        }
