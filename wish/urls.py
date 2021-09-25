from django.urls import path
from wish.apis import api_wish_me_birthday

urlpatterns = [
    path('birthday/', api_wish_me_birthday, name="wish-me-birthday"),
]
