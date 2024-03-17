import os

from dotenv import load_dotenv

class LoadEnviroment:
    """
    A class that represents the environment settings for the AI models.

    Attributes:
        hugging_face_key (str): The API key for Hugging Face.
        openai_api_key (str): The API key for OpenAI.
    """

    def __init__(self):
        """
        Initializes the LoadEnviroment object.

        It loads the environment variables and sets the AI keys.
        """
        load_dotenv()
        self.set_ai_keys()

    def set_ai_keys(self):
        """
        Sets the AI keys based on the environment variables.

        If the HUGGING_FACE_KEY environment variable is set, it assigns its value to the hugging_face_key attribute.
        If the OPENAI_API_KEY environment variable is set, it assigns its value to the openai_api_key attribute.
        """
        if os.getenv("HUGGING_FACE_KEY") is not None or os.getenv("HUGGING_FACE_KEY") != "":
            self.hugging_face_key = os.getenv("HUGGING_FACE_KEY")
        elif os.getenv("OPENAI_API_KEY") is not None or os.getenv("OPENAI_API_KEY") != "":
            self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def set_hugging_face_key(self):
        """
        Returns the value of the HUGGING_FACE_KEY environment variable.

        Returns:
            str: The value of the HUGGING_FACE_KEY environment variable.
        """
        return os.getenv("HUGGING_FACE_KEY")
    
    def set_openai_api_key(self):
        """
        Returns the value of the OPENAI_API_KEY environment variable.

        Returns:
            str: The value of the OPENAI_API_KEY environment variable.
        """
        return os.getenv("OPENAI_API_KEY")

    def get_hugging_face_key(self):
        """
        Returns the Hugging Face API key.

        Returns:
            str: The Hugging Face API key.
        """
        return self.hugging_face_key

    def get_openai_api_key(self):
        """
        Returns the OpenAI API key.

        Returns:
            str: The OpenAI API key.
        """
        return self.openai_api_key

