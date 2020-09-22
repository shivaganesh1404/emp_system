from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer, ProfileViewSerializer
from rest_framework.decorators import api_view


@api_view(["GET", "POST", "PUT", "DELETE"])
def user(request):
    if request.method == 'POST':
        email = request.data.get("email")
        mobile_number = request.data.get("mobile_number")
        user_email = UserProfile.objects.filter(email=email)
        user_mob = UserProfile.objects.filter(mobile_number=mobile_number)
        if len(user_email) == 0:
            if len(user_mob) == 0:
                profile = UserProfile.objects.all()
                profile_serializer = UserProfileSerializer(data=request.data)
                if profile_serializer.is_valid():
                    profile_serializer.save()
                    return output("Successfull", profile_serializer.data, status.HTTP_201_CREATED)
                return output("Failed", profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
            else:
                return output("User with this mobile number already exist", [], status.HTTP_400_BAD_REQUEST)
        else:
            return output("User with this email id already exist", [], status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        id = request.GET.get('id')
        if id is None:
            try:
                profile = UserProfile.objects.all()
                serializer = ProfileViewSerializer(profile, many=True)
                return output("Successfull", serializer.data, status.HTTP_201_CREATED)

            except KeyError:
                return output("Error", [], status.HTTP_400_BAD_REQUEST)
        else:
            try:
                profile = UserProfile.objects.get(id=id)
                serializer = ProfileViewSerializer(profile, many=False)
                return output("Successfull", serializer.data, status.HTTP_201_CREATED)

            except KeyError:
                return output("Error", [], status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id = request.data.get("id")
        profile = request.data
        try:
            user = UserProfile.objects.filter(id=id)
            user.update(**profile)
            profile = UserProfile.objects.get(id=id)
            serializer = UserProfileSerializer(profile)
            return output("User Updated successfully", serializer.data, status.HTTP_200_OK)

        except KeyError:
            return output("Error", [], status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = request.GET.get("id")
        try:
            u = UserProfile.objects.filter(id=id)
            if len(u) != 0:
                u.delete()
                return output("User deleted successfully", [], status.HTTP_200_OK)
            else:
                return output("User  Not Found", [], status.HTTP_404_NOT_FOUND)
        except:
            return output("User  Not Found", [], status.HTTP_404_NOT_FOUND)


def output(message, data, status):
    response = [{
        "message": message,
        "status": status,
        "data": [data]
    }]
    return Response(response, status=status)


@api_view(["POST"])
def login(request):
    try:
        if request.method == "POST":
            email = request.data.get("email")
            password = request.data.get("password")
            u = UserProfile.objects.filter(email=email, password=password)
            if len(u) != 0:
                return output("success", ["User logged in Successfully"], status.HTTP_200_OK)
            else:
                pr_username = "admin@gmail.com"
                pr_password = "123456"

                if email == pr_username :
                    if password == pr_password:
                        return output("success", ["User logged in Successfully"], status.HTTP_200_OK)
                    else:
                        return output("Check the password entered", [], status.HTTP_200_OK)
                else:
                    return output("Check the email entered", [], status.HTTP_200_OK)

    except KeyError:
        return output("Error", [], status.HTTP_400_BAD_REQUEST)















