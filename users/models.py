from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # No additional fields are added, but you can add them as needed
    # Inherits fields like username, password, email, first name, last name, etc. from AbstractUser

    # Customizing the string representation of the model to display the email
    def __str__(self):
        return self.email
