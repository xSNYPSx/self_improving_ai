import os
import sys
import subprocess

# Устанавливаем кодировку консоли в UTF-8
os.system("chcp 65001")

def run_commands_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file, open('result.txt', 'w', encoding='utf-8') as result_file, open('log.txt', 'a', encoding='utf-8') as log_file:
        lines = file.readlines()

        for line in lines:
            command = line.strip()  # Удаляем пробелы и символы перевода строки
            if command:  # Проверяем, что команда не пустая
                print(f'Executing: {command}')
                try:
                    result = subprocess.run(command, shell=True, timeout=20, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    print(result.stdout)
                    result_file.write(f'{command}\n')  # Записываем команду в файл результатов
                    result_file.write(f'{result.stdout}\n\n')  # Записываем результат в файл результатов

                    # Сохранение ответа в файл log.txt
                    generated_response = result.stdout
                    comment = "Start of computer answer--->"
                    comment2 = "<---End of computer answer"
                    formatted_text = " " + comment + " " + generated_response + " " + comment2 + " "
                    log_file.write(formatted_text)
                    log_file.write("\n")  # Добавление новой строки

                except subprocess.CalledProcessError as e:
                    print(f"Error: {e.stdout}")
                    result_file.write(f'{command}\n')  # Записываем команду в файл результатов
                    result_file.write(f'Error: {e.stdout}\n\n')  # Записываем ошибку в файл результатов

                    # Сохранение ошибки в файл log.txt
                    generated_response = e.stderr
                    comment = "Start of computer answer--->"
                    comment2 = "<---End of computer answer"
                    formatted_text = " " + comment + " " + generated_response + " " + comment2 + " "
                    log_file.write(formatted_text)
                    log_file.write("\n")  # Добавление новой строки

                except subprocess.TimeoutExpired as e:
                    print("Command timed out.")
                    result_file.write(f'{command}\n')  # Записываем команду в файл результатов
                    result_file.write("Command timed out.\n\n")  # Записываем превышение времени ожидания в файл результатов

                    # Сохранение превышения времени ожидания в файл log.txt
                    generated_response = "Command timed out."
                    comment = "Start of computer answer--->"
                    comment2 = "<---End of computer answer"
                    formatted_text = " " + comment + " " + generated_response + " " + comment2 + " "
                    log_file.write(formatted_text)
                    log_file.write("\n")  # Добавление новой строки

if __name__ == '__main__':
    run_commands_from_file('command.txt')
