from dtu_user import DtuUser
from authentication_error import AuthenticationError
import requests, xmltodict

class Inside:
    API_URL = "https://cn.inside.dtu.dk/"
    API_HEADERS = {'X-appname': 'Project Manager', 'X-token': '440ca8a8-ae8c-477d-96ec-c15a5ea4b991'}

    def __init__(self, user: DtuUser):
        self.user = user
    
    def fetch_secure_password(self):
        if self.user.secure_password == None:
            pass
        
        credentials = {'username': self.user.study_id, 'password': self.user.password}

        with requests.Session() as s:
            s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})

            res = s.post("https://auth.dtu.dk/dtu/mobilapp.jsp", data=credentials)
        
            password = xmltodict.parse(res.text)["xml"]

            try:
                limited_access = password['LimitedAccess']
                secure_password = limited_access['@Password']
                self.user.secure_password = secure_password
            except KeyError:
                blocked_access = password['BlockedAccess']

                if blocked_access["@Reason"] == "IpWrongUserCredentials":
                    raise AuthenticationError("Wrong user credentials", None)
                return
                    