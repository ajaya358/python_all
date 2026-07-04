# Mocking - Replace real dependencies with fake ones in tests
# pip install pytest pytest-mock

import pytest
from unittest.mock import MagicMock, patch, AsyncMock

# --- Code to test ---
import requests

def get_weather(city: str) -> dict:
    response = requests.get(f"https://api.weather.com/v1/{city}")
    return response.json()

def send_email(to: str, subject: str) -> bool:
    # Imagine this calls an email API
    response = requests.post("https://api.email.com/send", json={"to": to, "subject": subject})
    return response.status_code == 200

class UserService:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.find_one({"id": user_id})

    def create_user(self, name: str, email: str):
        user = {"id": 1, "name": name, "email": email}
        self.db.insert(user)
        send_email(email, "Welcome!")
        return user

# --- Tests with mocking ---

# Mock external HTTP call
def test_get_weather(mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {"city": "Chennai", "temp": 35}
    mocker.patch("requests.get", return_value=mock_response)

    result = get_weather("Chennai")
    assert result["city"] == "Chennai"
    assert result["temp"] == 35

# Mock with patch decorator
@patch("requests.post")
def test_send_email(mock_post):
    mock_post.return_value.status_code = 200
    result = send_email("ajay@email.com", "Hello")
    assert result is True
    mock_post.assert_called_once()

# Mock database
def test_get_user():
    mock_db = MagicMock()
    mock_db.find_one.return_value = {"id": 1, "name": "Ajay"}

    service = UserService(mock_db)
    user = service.get_user(1)

    assert user["name"] == "Ajay"
    mock_db.find_one.assert_called_once_with({"id": 1})

@patch("requests.post")
def test_create_user(mock_post):
    mock_post.return_value.status_code = 200
    mock_db = MagicMock()

    service = UserService(mock_db)
    user = service.create_user("Ajay", "ajay@email.com")

    assert user["name"] == "Ajay"
    mock_db.insert.assert_called_once()
    mock_post.assert_called_once()  # email was sent

# Mock return different values each call
def test_multiple_calls(mocker):
    mock_fn = MagicMock(side_effect=[1, 2, 3])
    assert mock_fn() == 1
    assert mock_fn() == 2
    assert mock_fn() == 3

# Mock raises exception
def test_db_error():
    mock_db = MagicMock()
    mock_db.find_one.side_effect = Exception("DB connection failed")

    service = UserService(mock_db)
    with pytest.raises(Exception, match="DB connection failed"):
        service.get_user(1)

# Run: pytest test_mocking.py -v
