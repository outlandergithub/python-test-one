import requests
import pytest

def test_response_404():
    get_response = requests.get("https://api.github.com//orgs/outlander/repos")
    projects = get_response.json()
    #print(type(projects))
    #print(projects)        
    #for project in projects:
    #    print(f"Name: {project['name']}, and url: {'web_url'}")    
    assert get_response.status_code == 404

if requests.get("https://api.restful-api.dev/objects").status_code == 405:
    print("\n"
    "-----------------------------------------------------------------\n"
    "API REQUESTS BLOCKED WITH 405 METHOD NOT ALLOWED ERROR FROM API PROVIDER DUE TO DAILY LIMIT END\n"
    "-----------------------------------------------------------------\n"
    "We are very sorry but you reached your limit of requests per day. \n"
    "Our current limit is equal to 100 requests per day. \n"
    "The reason for that is the fact that servers cost money and 200 requests per user per day is all that we can afford at the moment. \n"
    "Tomorrow the limit will reset and you will be able to continue. Thanks and have a good day!")

else:

    @pytest.fixture
    def obj_id():
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
            }
        }
        print("Creating new product")
        response = requests.post("https://api.restful-api.dev/objects", json=payload)
        response_json = response.json()
        yield response_json["id"]
        requests.delete(f'https://api.restful-api.dev/objects/{response_json["id"]}', json=payload)

    def test_create_object():
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
            }
        }
        response = requests.post("https://api.restful-api.dev/objects", json=payload)
        response_json = response.json()
        print(response_json["name"])
        assert response.status_code == 200
        assert payload["name"] == response_json["name"]

    def test_get_object(obj_id):
        print(obj_id)
        response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
        response_json = response.json()
        assert response.status_code == 200
        assert obj_id == response_json["id"]

    def test_update_object(obj_id):
        print(obj_id)
        payload = {
            "name": "EDITED NAME",
            "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
            }
        }
        response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
        response_json = response.json()
        print(response_json["name"] + " of " + response_json["id"])
        assert response.status_code == 200
        assert payload["name"] == response_json["name"]

    def test_delete_object(obj_id):
        print(obj_id)
        response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
        response_json = response.json()
        expected_response_message = "Object with id = " + obj_id + ", has been deleted."
        print(expected_response_message)
        assert response.status_code == 200
        #assert response_json["message"] == expected_response_message
        new_response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}")
        new_response_json = response.json()
        new_expected_response_message = "Oject with id=" + obj_id + "was not found."
        print(new_expected_response_message)
        assert new_response.status_code == 404
        #assert new_response_json["error"] == new_expected_response_message