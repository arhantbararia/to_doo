from rest_framework.decorators import api_view
from .serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token





@api_view(['POST'])
def logout_view(request):
    
    try:
        request.user.auth_token.delete()
    
    except AttributeError:
        data = {"Error" : "BAD REQUEST"}
        
        return Response(data, status = status.HTTP_400_BAD_REQUEST)

    return Response(status = status.HTTP_200_OK)
    



@api_view(["POST"])
def registration_view(request):
    serializer = RegistrationSerializer(data = request.data)

    data = {}

    if(serializer.is_valid()):
        account = serializer.save()

        data['response'] = "Registration Sccessfull"
        data['username'] = account.username
        
        token = Token.objects.get(user = account ).key
        data['token'] = token

    else:
        data = serializer.errors

    return Response(data)


