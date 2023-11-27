import requests

def main():
    # response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP")
    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {
        'apikey': '86OyucJHrWF5Mzg92fVawFmywCyl0KW6'
    }
    payload = {"base": "USD", "symbols": "SEK"}
    response = requests.get(url,
                            headers=headers,params=payload)

    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")

    data = response.json()
    print("JSON data: ", data)



if __name__ == "__main__":
    main()