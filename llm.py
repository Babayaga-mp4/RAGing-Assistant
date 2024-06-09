# from openai import embeddings
import ollama
from openai import OpenAI, Stream
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
# from openai.types.chat.chat_completion_message import ChatCompletionMessage

from constants import MESSAGE_TEMPLATE, SYSTEM_MESSAGE


class ChatBot():
    def __init__(self) -> None:
        self.client = OpenAI()
        pass

    def chatty_boi(self, context, query, history) -> Stream[ChatCompletionChunk]:
        formatted_message = {
            "role": MESSAGE_TEMPLATE["role"],
            "content": MESSAGE_TEMPLATE["content"].format(query=query, context=context)
        }
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            SYSTEM_MESSAGE,
            *history,
            formatted_message
        ],
        stream=True
        )

        return completion
    
    def open_chatty_boi(self, context, query, history):
        # Handles Open Source LLMs
        # To make sure the model is online, inside the docker, RUN ollama pull llama3 phi3:3.8b-mini-128k-instruct-q2_K 
        formatted_message = {
            "role": MESSAGE_TEMPLATE["role"],
            "content": MESSAGE_TEMPLATE["content"].format(query=query, context=context)
        }
        completion = ollama.chat(
            model='phi3:3.8b-mini-128k-instruct-q2_K', # Change it to one of the supported ollama models and make sure it is available.
            messages=[
                SYSTEM_MESSAGE,
                *history,
                formatted_message
            ],
            stream=True,
        )

        return completion