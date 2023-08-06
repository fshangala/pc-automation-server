from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from django.http.request import parse_qsl
from rich import print

@database_sync_to_async
def get_token_user(token:str):
  try:
    return Token.objects.get(key=token).user
  except Exception as e:
    return AnonymousUser()

class TokenAuthMiddleWare:
  def __init__(self,app):
    self.app = app
    
  async def __call__(self, scope, receive, send):
    query_string = dict(parse_qsl(scope["query_string"].decode("utf8")))
    token = query_string["token"]
    token_user = await get_token_user(token)
    scope["user"] = token_user
    
    return await self.app(scope,receive,send)
    