from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import keys
import messages
from wish import serializers
from wish.helper import HelperValidation


@swagger_auto_schema(
    operation_id='Wish Birthday',
    method='get',
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=False)
    ],
    responses={
        200: serializers.WishMeResponse,
        400: 'Error when the name is not valid'
    }
)
@api_view(['GET'])
def api_wish_me_birthday(request):
    """
    The API takes only one parameter called `name` as input and returns a string wishing happy birthday that
    uses the value in the name parameter as output. e.g., if the value of the `name` parameter is Elon Musk,
    then API returns *“Happy Birthday,* Elon Musk*!”*
    """
    print("**** Wish Me Birthday ****")

    # Get request data
    req_name = request.GET.get(keys.NAME, '')

    # Validate name for empty value
    if req_name == '':
        return Response(data={keys.MESSAGE: messages.ENTER_SOME_VALUE}, status=status.HTTP_400_BAD_REQUEST)

    # Validate name for correct value
    if not HelperValidation.is_valid_name(req_name):
        return Response(data={keys.MESSAGE: messages.NAME_NOT_VALID}, status=status.HTTP_400_BAD_REQUEST)

    # Create a wish string
    my_wish = messages.HAPPY_BIRTHDAY_FRIEND.format(name=req_name)

    # print and return wish
    print(my_wish)
    return Response(data={keys.MESSAGE: my_wish})
