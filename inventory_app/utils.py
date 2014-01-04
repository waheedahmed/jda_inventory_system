from datetime import datetime
from django.contrib.auth import authenticate

__author__ = 'Waheed'

def authenticate_user(request, username, password):
  user = authenticate(username=username, password=password)
  success = False
  if user is not None and user.is_active:
    success = custom_login(request, user, user.backend)
  return success

def custom_login(request, user, backend):
  try:
    SESSION_KEY = '_auth_user_id'
    BACKEND_SESSION_KEY = '_auth_user_backend'
    user.last_login = datetime.now()
    user.save()
    if SESSION_KEY in request.session:
      if request.session[SESSION_KEY] != user.id:
        # To avoid reusing another user's session, create a new, empty
        # session if the existing session corresponds to a different
        # authenticated user.
        request.session.flush()
    else:
      request.session.cycle_key()
    request.session[SESSION_KEY] = user.id
    request.session[BACKEND_SESSION_KEY] = backend
    if hasattr(request, 'user'):
      request.user = user
    return True
  except:
    return False
