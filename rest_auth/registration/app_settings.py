from django.conf import settings
from rest_framework.permissions import AllowAny

from rest_auth.registration.serializers import (
    RegisterSerializer as DefaultRegisterSerializer,
    SocialSignUpSerializer as DefaultSocialRegisterSerializer
)
from ..utils import import_callable

serializers = getattr(settings, 'REST_AUTH_REGISTER_SERIALIZERS', {})

RegisterSerializer = import_callable(
    serializers.get('REGISTER_SERIALIZER', DefaultRegisterSerializer))

SocialRegisterSerializer = import_callable(
    serializers.get('SOCIAL_REGISTER_SERIALIZER', DefaultSocialRegisterSerializer))


def register_permission_classes():
    permission_classes = [AllowAny, ]
    for klass in getattr(settings, 'REST_AUTH_REGISTER_PERMISSION_CLASSES', tuple()):
        permission_classes.append(import_callable(klass))
    return tuple(permission_classes)
