from rest_framework_api_key.models import APIKey


def generate_api_key():
    _, api_key = APIKey.objects.create_key(name="my-remote-service")
    return api_key
