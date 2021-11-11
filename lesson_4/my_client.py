import requests
from os import getenv
# response = requests.post("http://localhost:5001/whatismyname")


def test_get(url_to_test):
    response = requests.get(f"http://{url_to_test}/whatismyname")
    actual = response.text
    expected = "mazda, citroen, chevrolet"
    assert actual == expected


def test_post(url_to_test):
    response = requests.post(f"http://{url_to_test}/whatismyname")
    actual = response.text
    expected = "saved new car"
    assert actual == expected


def test_get_cars(url_to_test):
    response = requests.get(f"http://{url_to_test}/cars")
    my_file = open("my_cars.txt")
    expected = str(my_file.readlines())
    actual = response.text
    assert actual == expected


# test_get(getenv("BASE_URL", "localhost:5001"))
test_post("localhost:5001")
test_get_cars("localhost:5001")
