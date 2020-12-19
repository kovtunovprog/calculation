from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(username, password):
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return user
