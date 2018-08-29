import requests, json

API_URL = "http://api:5000"

def urlencode(s):
    return s.replace("#", "%23")

def get_user(discord_id):
    discord_id = urlencode(discord_id)
    with requests.Session() as s:
        res = s.get(f"{API_URL}/user/{discord_id}")

        if res.status_code == 404:
            return None

        return res.json()

def get_or_create(discord_id):
    discord_id = urlencode(discord_id)
    with requests.Session() as s:
        res = s.get(f"{API_URL}/login/{discord_id}")

        j = res.json()
        if res.status_code == 201:
            return f"{API_URL}/?connect={j['token']}"

def main():
    user = get_user("algorythm#0001")
    print(user)

if __name__ == '__main__':
    main()