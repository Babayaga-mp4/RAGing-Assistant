import openai

openai.api_key = "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"

def get_response(user_query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": user_query}
        ],
        stream=True
    )
    for chunk in response:
        print(chunk.choices[0].delta.get('content'))
    
    return response



def handle_chat():
    user_query = input("Whats on your mind today?\n")
    response = get_response(user_query)
    reply = response['choices'][0]['message']['content']
    print(reply)

while True:
    handle_chat()