# github_manager/github_manager.py

from abc import ABC, abstractmethod

class GitHubManager(ABC):
    @abstractmethod
    def create_repository(self) -> str:
        """
        Abstract method to create a GitHub repository.
        :return: URL of the created repository.
        """
        pass

    @abstractmethod
    def run(self):
        """
        Abstract method to handle the main workflow.
        """
        pass
