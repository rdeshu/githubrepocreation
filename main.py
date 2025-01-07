# main.py

from github_manager.github_manager_impl import GitHubManagerImpl
from params import Parameters

if __name__ == "__main__":
    # Initialize parameters
    parameters = Parameters()

    # Gather user input
    print("Welcome to GitHub Repository Creation Tool!")
    github_token = input("Enter your GitHub personal access token: ").strip()
    repo_name = input("Enter the repository name: ").strip()
    repo_description = input("Enter the repository description (optional): ").strip() or None
    organization_name = input("Enter the organization name (leave blank for personal repository): ").strip() or None

    # Set parameters dynamically
    parameters.set_params(
        github_token=github_token,
        repo_name=repo_name,
        repo_description=repo_description,
        organization_name=organization_name
    )

    # Run GitHubManager
    manager = GitHubManagerImpl(parameters)
    manager.run()
