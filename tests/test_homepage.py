import requests
from bs4 import BeautifulSoup

BASE_URL = "http://localhost:8000"
response = requests.get(BASE_URL)

# Using HTML to account for minification and malformed HTML
soup = BeautifulSoup(response.text, "html5lib")


def test_homepage():
    """
    # Test the homepage
    """
    assert response.status_code == 200


def test_title():
    """
    # Test the title
    """
    title = soup.find("title")

    # Test the title exits
    assert title is not None
    print(title)

    # Test the title contains the correct text
    assert title.text.strip() == "The absolutely obsolete dev"