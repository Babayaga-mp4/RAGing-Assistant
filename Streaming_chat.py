import grpc
import generated_code_from_proto  # Replace with the actual module name

channel = grpc.insecure_channel('localhost:50051')
stub = generated_code_from_proto.ChatAssistantStub(channel)
response_iterator = stub.GetResponse(generated_code_from_proto.UserQuery(content="Your user query here"))
for response in response_iterator:
    print(response.content)
