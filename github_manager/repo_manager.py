# github_manager/repo_manager.py

import requests
from authentication import Authentication

class RepoManager:
    def __init__(self, parameters):
        self.parameters = parameters

    def create_repository(self) -> str:
        """
        Creates a new GitHub repository using the provided parameters.

        :return: URL of the created repository.
        """
        if not self.parameters.repo_name:
            raise ValueError("Repository name is required.")

        # Determine the API endpoint based on the organization name
        if self.parameters.organization_name:
            url = f"{self.parameters.api_url}/orgs/{self.parameters.organization_name}/repos"
        else:
            url = f"{self.parameters.api_url}/user/repos"

        headers = Authentication.get_headers(self.parameters)
        data = {
            "name": self.parameters.repo_name,
            "description": self.parameters.repo_description,
            "private": False,
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            return response.json()['html_url']
        else:
            raise Exception(f"Failed to create repository: {response.status_code}, {response.text}")
