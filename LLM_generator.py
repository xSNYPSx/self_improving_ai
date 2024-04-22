import os
import sys
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1263/v1", api_key="not-needed")

def process_prompt_and_log():
    # Read the answers from the text file
    with open("prompt.txt", "r", encoding="utf-8") as file:
        prompt = file.read().strip()

    # Read the answers from the text file
    with open("log.txt", "r", encoding="utf-8") as file:
        log = file.read().strip()

    try:
        completion = client.chat.completions.create(
          model="local-model",  # this field is currently unused
          messages=[
            {"role": "system", "content": f"Initial prompt: {prompt}, Current log: {log}"},
            {"role": "user", "content": f"Follow your prompt"}  # Use the question from the file
          ],
          temperature=0.7,
          max_tokens=1000
        )

        generated_response = completion.choices[0].message.content.split('#', 1)[0]

        # Сохранение ответа в файл text.txt
        with open("answer.txt", "w", encoding="utf-8") as file:
            comment = ""
            formatted_text = comment + "" + generated_response
            file.write(formatted_text)
            file.write("\n")  # Добавление новой строки

        # Сохранение ответа в файл text.txt
        with open("log.txt", "a", encoding="utf-8") as file:
            comment = "Start of your previous message--->"
            comment2 = "<---End of your previous message"
            formatted_text = " " + comment + " " + generated_response + " " + comment2 + " "
            file.write(formatted_text)
            file.write("\n")  # Добавление новой строки

        print(generated_response)

    except openai.BadRequestError as e:
        if 'Context Overflow Policy Error' in str(e):
            print("Error: Too many tokens. Running script token_clear.py")
            os.system('python token_clear.py')
            sys.exit(1)
        else:
            raise e

process_prompt_and_log()
