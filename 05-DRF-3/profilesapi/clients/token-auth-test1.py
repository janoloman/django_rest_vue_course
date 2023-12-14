import requests

def client():
  # credentials = {"username": "admin", "password": "wildsense"}
  # response = requests.post("http://127.0.0.1:8000/api/dj-rest-auth/login/",
  #                          data=credentials)

  token_h = "Token c8ed4e99b53733ff0b6255f93b5dd08198352bff"
  headers = {"Authorization": token_h}
  response = requests.get("http://127.0.0.1:8000/api/profiles/",
                          headers=headers)

  print("Status Code: ", response.status_code)
  response_data = response.json()
  print(response_data)


if __name__== "__main__":
  client()