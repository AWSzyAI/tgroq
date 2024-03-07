import asyncio
import argparse
from groq import AsyncGroq

history = []

async def main(message):
    client = AsyncGroq()

    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=False,
    )
    response_content = chat_completion.choices[0].message.content
    print('<<< Jarvis: ', end="", flush=True)
    print(response_content)

    return response_content

def update_history(user_message, response):
    if user_message:
        history.append({"role": "user", "content": user_message})
    if response:
        history.append({"role": "assistant", "content": response})

def prepare_message_with_history():
    combined_message = ""
    for message in history[-10:]:
        combined_message += f"{message['role']}: {message['content']}\n"
    return combined_message

async def chat(user_text=None):
    if user_text is None:
        while True:
            user_text = input('>>> User: ')
            message_with_history = prepare_message_with_history() + user_text
            response = await main(message_with_history)
            update_history(user_text, response)
    else:
        message_with_history = prepare_message_with_history() + user_text
        response = await main(message_with_history)
        update_history(user_text, response)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("message", nargs='?', default=None, help="The message to send to the chatbot")
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(chat(args.message))
    except KeyboardInterrupt:
        print("Chat session ended.")
    finally:
        loop.close()