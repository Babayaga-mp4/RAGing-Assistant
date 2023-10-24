import grpc
from concurrent import futures
import time
import generated_code_from_proto  # Replace with the actual module name


class ChatAssistantServicer(generated_code_from_proto.ChatAssistantServicer):
    def GetResponse(self, request, context):
        # This is where you would interface with the OpenAI API
        # You can yield the response in chunks, simulating "typing"
        for chunk in get_chunks_from_openai_api(request.content):
            yield generated_code_from_proto.AssistantReply(content=chunk)
            time.sleep(0.05)  # Typing delay

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
generated_code_from_proto.add_ChatAssistantServicer_to_server(ChatAssistantServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
