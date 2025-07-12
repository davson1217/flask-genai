from abc import ABC, abstractmethod

class ChatModel(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass