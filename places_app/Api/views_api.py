from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from places_app.serialization import ItemLocationSerializers, UserPSerializers
from places_app.models import UserP, ItemLocation

path = r"C:\Users\rotem\OneDrive\Desktop\my_project\rentmyplace\\places_app\\statics"


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def check_token(request):
    try:
        return Response({"message": "token is valid", 'user': request.user.username})
    except Exception as e:
        return Response({"message": e}, status=400)


@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    password = request.data.get("password")
    email = request.data.get("email", '')
    phone = request.data.get("phone", 000000000)
    address = request.data.get("address", '')
    type = request.data.get("type", 'Private')
    user = User.objects.create_user(username=username, email=email, password=password)
    user_p = UserP.objects.create(user=user, first_name=first_name, last_name=last_name, phone=phone, address=address,
                                  type=type)
    token = Token.objects.create(user=user)
    data = {'user': user, 'token': token}
    return JsonResponse({"id": user_p.id, "token": str(token)})



@api_view(['POST'])
def update(request):
    try:
        user_id = request.data.get("user_id")
        user = User.objects.filter(id=user_id).first()
        if user is None:
            return Response({"error": "User not found."}, status=404)

        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")
        email = request.data.get("email")
        phone = request.data.get("phone")
        address = request.data.get("address")

        userp = UserP.objects.filter(id=user_id).first()
        if userp:
            if first_name != '':
                userp = UserP.objects.filter(id=user_id).update(first_name=first_name)
            if last_name != '':
                userp = UserP.objects.filter(id=user_id).update(last_name=last_name)
            if phone != '':
                userp = UserP.objects.filter(id=user_id).update(phone=phone)
            if address != '':
                userp = UserP.objects.filter(id=user_id).update(address=address)
            userp.save()

        if user.is_valid():
            user = user.save()
            user.set_password(password)
            user.save()

        if email != " ":
            user.set_email(email)
            user.save()

        return Response({f"success": f"User updated successfully.{first_name}"})

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['POST'])
def delete_user(request):
    username = UserP.user.objects.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone = request.data.get("phone", 000000000)
    address = request.data.get("address", '')
    type = request.data.get("type", 'Private')
    user = username.delete()
    user_p = UserP.objects.delete(user=user, first_name=first_name, last_name=last_name, phone=phone, address=address,
                                  type=type)
    return Response(f"user is deleted:{user_p}")


@api_view(['POST'])
def search_user(request):
    list_all_users = UserP.objects.all()
    list = UserPSerializers(list_all_users, many=True)
    return Response(list.data)


@api_view(['POST'])
def search_this_user(request):
    username = request.data.get("username")
    if username:
        filtered_users = UserP.objects.filter(user__username__icontains=username)
        serialized_data = UserPSerializers(filtered_users, many=True, context={'request': request})
        return Response(serialized_data.data)
    else:
        return Response([])


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


@api_view(['POST'])
def create_item(request):
    user_id = request.data.get("user_id")
    user = User.objects.filter(id=user_id)
    if len(user) == 0:
        return Response("error")

    user = user[0]
    owner = user
    item_name = request.data.get("item_name")
    num_people = request.data.get("num_people")
    city = request.data.get("city")
    picture_location = request.data.get("picture_location")

    if isinstance(picture_location, str):
        picture_path = picture_location
    else:
        picture_file = picture_location.file
        if hasattr(picture_file, 'name'):
            picture_path = default_storage.save(picture_file.name, picture_file)
        else:
            picture_name = default_storage.get_valid_name("uploaded_file")
            picture_path = default_storage.save(picture_name, picture_file)

    new_item = ItemLocation.objects.create(item_name=item_name, num_people=num_people, owner=owner, city=city,
                                           picture_location=picture_path)

    return JsonResponse({"id": new_item.id})


@api_view(['DELETE'])
def delete_item(request, item_id):
    try:
        item = ItemLocation.objects.get(id=item_id)
        item.delete()
        return Response({"message": "Item deleted successfully"})
    except ObjectDoesNotExist:
        return Response({"error": "Item not found"}, status=404)
    except Exception as e:
        return Response({"error": "An error occurred while deleting the item"}, status=500)


@api_view(['DELETE'])
def delete_item(request,item_id):
    try:
        item = ItemLocation.objects.get(id=item_id)
        item.delete()
        return Response({"message": "Item deleted successfully"})
    except ItemLocation.DoesNotExist:
        return Response({"error": "Item not found"}, status=400)

@api_view(['POST'])
def update_item(request):
    numb = ItemLocation.objects.get(id='2')
    item_name = request.data.get("item_name")
    num_people = request.data.get("num_people")
    city = request.data.get("city")
    if item_name != '':
        item_p = ItemLocation.objects.filter(id=numb.id).update(item_name=item_name)
    if num_people != '':
        item_p = ItemLocation.objects.filter(id=numb.id).update(num_people=num_people)
    if city != '':
        item_p = ItemLocation.objects.filter(id=numb.id).update(city=city)
    return Response(f" the city in {numb} sucssed")


@api_view(['POST'])
def search_items(request):
    item_name = request.data.get("item_name", '')
    num_people = request.data.get("num_people", '')
    owner = request.data.get("owner", '')
    city = request.data.get("city", '')
    if item_name != '' and num_people == '' and owner == '' and city == '':
        item_n = ItemLocation.objects.filter(item_name=item_name)
        item = ItemLocationSerializers(item_n, many=True)
        return Response(item.data)
    elif item_name == '' and num_people != '' and owner == '' and city == '':
        item_num = ItemLocation.objects.filter(num_people=num_people)
        item = ItemLocationSerializers(item_num, many=True)
        return Response(item.data)
    elif item_name == '' and num_people == '' and owner != '' and city == '':
        item_owner = ItemLocation.objects.filter(owner=owner)
        item = ItemLocationSerializers(item_owner, many=True)
        return Response(item.data)
    elif item_name == '' and num_people == '' and owner == '' and city != '':
        item_city = ItemLocation.objects.filter(city=city)
        item = ItemLocationSerializers(item_city, many=True)
        return Response(item.data)
    elif item_name == '' and num_people == '' and owner == '' and city == '':
        list_all_items = ItemLocation.objects.all()
        all_items = ItemLocationSerializers(list_all_items, many=True)
        return Response(all_items.data)


