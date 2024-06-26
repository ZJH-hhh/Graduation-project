from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models import NewUser
from django.contrib.auth.models import User


class InfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id', 1))
            print(user_id)
            user = NewUser.objects.get(id=user_id)
            return Response({
                'username': user.username,
                'photo': user.photo,
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })