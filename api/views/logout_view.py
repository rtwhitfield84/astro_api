from django.contrib.auth.models import User
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class Logout(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        self.logout(request)

        return Response({"success": ("Successfully logged out.")},
                        status=status.HTTP_200_OK)