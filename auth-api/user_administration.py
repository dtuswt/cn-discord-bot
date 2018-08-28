from redis import Redis
from authentication_error import AuthenticationError
from dtu_user import DtuUser
from inside import Inside

def check_auth(username, password):
    user = DtuUser(username, password)
    inside = Inside(user)

    try:
        inside.fetch_secure_password()
    except AuthenticationError:
        return False
    return user.secure_password