import requests
import base64
from pprint import pprint as pp
client_id = '213fc90b1a9246409f43553fd76c6845'
client_secret = 'b27b5a4e5a974c16914ab91ab9968921'

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

token_url = 'https://accounts.spotify.com/api/token'
token_data = {
    'grant_type': 'client_credentials'
}
token_headers = {
    'Authorization': f'Basic {client_creds_b64}',
}

response = requests.post(token_url, data=token_data, headers=token_headers)

if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print(f"Access Token: {access_token}")
    with open("access_token.txt", "w") as f:
        f.write(access_token)
else:
    print(f"Failed to get token: {response.status_code}")

headers = {
    'Authorization': f'Bearer {access_token}',
}

artist_id = '1Xyo4u8uXC1ZmMpatF05PJ'
artist_ids = {'1Xyo4u8uXC1ZmMpatF05PJ'}
depth = 1
for i in depth:
    


artist_id = '1Xyo4u8uXC1ZmMpatF05PJ'
artist_url = f'https://api.spotify.com/v1/artists/{artist_id}/related-artists'

response = requests.get(artist_url, headers=headers)

if response.status_code == 200:
    artist_data = response.json()
    pp(len(artist_data['artists']))
else:
    print(f"Failed to get artist data: {response.status_code}")