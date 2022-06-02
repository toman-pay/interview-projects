from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from identity.managers.user_model_manager import UserModelManager


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254, min_length=3, required=True, allow_blank=False, allow_null=False)
    repeat_password = serializers.CharField(write_only=True, required=True, allow_blank=False)

    def create(self, validated_data):
        return UserModelManager().create_user(
            email=self.initial_data.get('email'),
            password=self.initial_data.get('password'))

    def validate_email(self, value: str) -> str:
        if self.Meta.model.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("A user with this email already exists."))

        return value

    def validate(self, attrs):
        errors: dict = dict()

        password: str = attrs.get('password')
        repeat_password: str = attrs.get('repeat_password')

        if password != repeat_password:
            errors['repeat_password'] = "Password and re-password do not match."

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    class Meta:
        model = get_user_model()

        fields = [
            'email',
            'password',
            'repeat_password',
            'id',
        ]

        extra_kwargs = {
            'password':
                {
                    'write_only': True,
                    'required': True,
                    'allow_blank': False,
                },
        }
