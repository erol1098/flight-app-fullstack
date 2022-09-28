from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators = [validators.UniqueValidator(queryset=User.objects.all())]
  )

  password = serializers.CharField(
    required=True,
    write_only=True,
    validators = [validate_password],
    style={"input_type":"password"}
  )
  password1 = serializers.CharField(
    required=True,
    write_only=True,
    validators = [validate_password],
    style={"input_type":"password"}
  )

  class Meta:
    model = User
    fields = (
      "username",
      "email",
      "first_name",
      "last_name",
      "password",
      "password1"
    )