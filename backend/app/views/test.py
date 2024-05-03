from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import NewUser


class TestView(APIView):
    def get(self, request):
        try:
            data = {'msg': 1}
            return Response({
                'result': 'success',
                'data': data,
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

    def post(self, request):
        try:
            user = NewUser(
                userid=20000000,
                role='stu',
                college='计算机学院',
                back_time='2000-01-02',
            )
            user.save()
            return Response({
                'result': 'success',
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })
