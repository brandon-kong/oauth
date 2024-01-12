from rest_framework import serializers

from core.user.models import User

class UserCreationSerializer(serializers.ModelSerializer):
    """
    Serializer for user creation
    """

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"}
            }
        }

    def create(self, validated_data):
        """
        Create user
        """

        user = User.objects.create_user(
            **validated_data
        )

        return user