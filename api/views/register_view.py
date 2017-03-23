from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
import json


class RegisterView(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)


    error_messages = {
    'invalid': 'Please enter a valid username or password',
    'disabled': 'Sorry, account suspended'
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
            })

    def post(self, request):
        """
        Purpose: Register a user
        Author: @rtwhitfield84
        """

        req_body = json.loads(request.body.decode())
        new_user = User.objects.create_user(
            username=req_body['username'],
            email=req_body['email'],
            password=req_body['password'],
            )

        success = False
        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
                data = json.dumps({
                    'success': True,
                    'username': new_user.username,
                    'email': new_user.email,
                })
                return HttpResponse(data, content_type='application/json')

            return HttpResponse(self._error_response('disabled'), content_type='application/json')
        return HttpResponse(self._error_response('invalid'), content_type='application/json')