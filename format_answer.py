# Открываем исходный файл для чтения
with open('answer.txt', 'r') as file:
    lines = file.readlines()

# Объявляем список для хранения выбранных команд
commands = []

# Флаг для отслеживания начала блока команд
inside_block = False
ask_human_block = False

# Перебираем строки файла
for line in lines:
    # Если встретили начало блока команд, устанавливаем флаг
    if '{command_start}' in line:
        inside_block = True
        continue
    # Если встретили конец блока команд, сбрасываем флаг
    if '{command_end}' in line:
        inside_block = False
        continue
    # Если встретили начало блока вопроса к человеку, устанавливаем флаг
    if '{ask_human}' in line:
        ask_human_block = True
        continue
    # Если встретили конец блока вопроса к человеку, сбрасываем флаг
    if '{end_ask_human}' in line:
        ask_human_block = False
        continue
    # Если флаг блока команд установлен, добавляем текущую строку в список команд
    if inside_block:
        commands.append(line.strip())
    # Если флаг блока вопроса к человеку установлен, выводим текущую строку на экран и запускаем скрипт
    if ask_human_block:
        print(line.strip())
        import subprocess
        subprocess.run(['python', 'human_question.py'])

# Открываем выходной файл для записи
with open('command.txt', 'w') as file:
    # Записываем в него команды, разделяя их переносом строки
    file.write('\n'.join(commands))
    input("Press Enter to close the window...")
