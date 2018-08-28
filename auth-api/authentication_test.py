from dtu_user import DtuUser
from inside import Inside
from authentication_error import AuthenticationError
from getpass import getpass

def test_credentials(study_id: str, password: str):
    user = DtuUser(study_id, password)
    inside = Inside(user)

    try:
        inside.fetch_secure_password()
    except AuthenticationError as e:
        print("Authentication failed!")
        return

    print(f"Your secure password is: {user.secure_password}.")

if __name__ == "__main__":
    print("Testing wrong credentiasl")
    test_credentials("s123123", "123456789")
    
    study_id = input("Username: ")
    password = getpass("Password: ")

    test_credentials(study_id, password)
