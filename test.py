import requests

def test():

    response = requests.get("http://127.0.0.1:5000/api/products/")
    print(response.json())


if __name__ == "__main__":
    test()