import pytest
import requests

RAPIDAPI_URL = "https://exercisedb.p.rapidapi.com/exercises/target/abductors?limit=10&offset=0"  # PAKEISK į tikrą URL
RAPIDAPI_HEADERS = {
    "X-RapidAPI-Key": "83d0b558d6msh8efcd43e1a7ef85p114ab3jsn636b00461c3a",  # gali naudoti .env arba pytest fixtures
    "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

def test_rapidapi_response_status():
    response = requests.get(RAPIDAPI_URL, headers=RAPIDAPI_HEADERS)
    assert response.status_code == 200

def test_rapidapi_response_structure():
    url = "https://exercisedb.p.rapidapi.com/exercises/target/abductors?limit=10&offset=0"
    headers = {
        "X-RapidAPI-Key": "83d0b558d6msh8efcd43e1a7ef85p114ab3jsn636b00461c3a",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        pytest.fail(f"Response is not JSON: {response.text}")

    assert isinstance(data, list), f"Expected list, got {type(data)}"
    assert len(data) > 0, "Returned list is empty"

    sample = data[0]
    assert "name" in sample, "Missing 'name' in exercise data"
    assert "target" in sample, "Missing 'target' in exercise data"
    assert "bodyPart" in sample, "Missing 'bodyPart' in exercise data"

