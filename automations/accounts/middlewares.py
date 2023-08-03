from rest_framework.authtoken.models import Token

class TokenAuthMiddleWare:
  def __init__(self,app):
    self.app = app
  async def __call__(self, scope, receive, send):
    token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]
    token_user = Token.objects.get(key=token).user
    scope["user"] = token_user
    return await super().__call__(scope,receive,send)
    