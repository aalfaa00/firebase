import json
from .models import UserToken
from .serializers import UserMessageSerializers, UserTokenSerializers
from rest_framework.views import APIView
from fcmmanager import FCMManager as fcm
from rest_framework.response import Response
from rest_framework import status

class CreateUserTokenView(APIView):
    def post(self, request):
        serializer = UserTokenSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        usertoken = UserToken.objects.all()
        serializer = UserTokenSerializers(usertoken, many=True)
        return Response(serializer.data)




class FirebaseView(APIView):
    def post(self, request, user_id):
        serializer = UserMessageSerializers(data=request.data)

        user_id = self.kwargs['user_id']
        profile_s = UserToken.objects.filter(user_id=user_id).exists()

        if profile_s:
            profile = UserToken.objects.get(user_id=user_id)
            tokens = [profile.token]

            if serializer.is_valid():
                message = serializer.data['message']    
                fcm.sendPush("hi", message, tokens)

                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Not profile', status=status.HTTP_400_BAD_REQUEST)

