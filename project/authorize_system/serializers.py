from rest_framework import serializers, validators
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',  'password','first_name', 'last_name')

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(),
                        'This email address is already exists'
                    )
                ],
            },
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        firstname = validated_data.get('firstname')
        lastname = validated_data.get('lastname')

        user = User.objects.all(
            username=username, password=password, email=email, firstname=firstname, lastname=lastname
        )
        return user
        # return super(self, user).create(validated_data)