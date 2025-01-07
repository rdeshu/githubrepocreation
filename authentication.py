# authentication.py

class Authentication:
    @staticmethod
    def get_headers(parameters):
        """
        Returns the headers required for GitHub API authentication.

        :param parameters: Instance of the Parameters class.
        :return: Dictionary containing authentication headers.
        """
        if not parameters.github_token:
            raise ValueError("GitHub token is not set. Please provide a valid token.")
        return {
            "Authorization": f"token {parameters.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
