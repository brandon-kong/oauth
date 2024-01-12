from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as DRFSJ_TokenObtainPairSerializer

from core.user.models import User

class TokenObtainPairSerializer(DRFSJ_TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token['user_implicit_id'] = str(user.implicit_id)

        return token