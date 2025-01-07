# params.py

class Parameters:
    def __init__(self):
        self.github_token = None
        self.api_url = "https://api.github.com"
        self.repo_name = None
        self.repo_description = "Created with GitHub Repo Creation Tool"
        self.organization_name = None

    def set_params(self, github_token, repo_name, repo_description=None, organization_name=None):
        """
        Sets the parameters dynamically.

        :param github_token: GitHub personal access token.
        :param repo_name: Repository name.
        :param repo_description: (Optional) Repository description.
        :param organization_name: (Optional) Organization name.
        """
        self.github_token = github_token
        self.repo_name = repo_name
        self.repo_description = repo_description or self.repo_description
        self.organization_name = organization_name
