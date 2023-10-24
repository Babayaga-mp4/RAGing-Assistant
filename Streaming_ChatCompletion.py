import grpc
from concurrent import futures
import time
import chat_pb2_grpc
import chat_pb2  # Replace with the actual module name
from QA_Scratch import get_chunks_from_openai_api

class ChatAssistantServicer(chat_pb2_grpc.ChatAssistantServicer):
    def GetResponse(self, request, context):
        # This is where you would interface with the OpenAI API
        # You can yield the response in chunks, simulating "typing"
        for chunk in get_chunks_from_openai_api(request.content):
            yield chat_pb2.AssistantReply(content=chunk)
            time.sleep(0.05)  # Typing delay

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
chat_pb2_grpc.add_ChatAssistantServicer_to_server(ChatAssistantServicer(), server)
server.add_insecure_port('localhost:50051')
server.start()
print("Server started. Listening on localhost:50051.")
try:
    while True:
        time.sleep(86400)  # Sleep for a day. The server will run indefinitely until interrupted.
except KeyboardInterrupt:
    server.stop(0)