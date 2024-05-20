import grpc
import chat_pb2
import chat_pb2_grpc
import sys

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatAssistantStub(channel)

    while True:
        # Get user input
        user_query = input("\nUser(type your query or 'exit' to quit): ")

        # Exit loop if user types 'exit'
        if user_query.lower() == 'exit':
            break

        print("\nAssistant: ", end="", flush=True)
        response_iterator = stub.GetResponse(chat_pb2.UserQuery(content=user_query))
        for response in response_iterator:
            print(response.content, end="", flush=True)
            sys.stdout.flush()
        print('\n')

if __name__ == '__main__':
    main()
