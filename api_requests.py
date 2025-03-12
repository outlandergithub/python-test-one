import requests
import unittest
import pytest
import selenium

get_response = requests.get("https://gitlab.cryptocommercial.dev/api/v4/users/outlander/projects")

projects = get_response.json()
print(type(projects))

for project in projects:
    print(f"Name: {project['name']}, and url: {'web_url'}")