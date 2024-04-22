import time
import subprocess

while True:
    subprocess.run(['python', 'LLM_generator.py'])
    subprocess.run(['python', 'format_answer.py'])
    subprocess.run(['python', 'executor.py'])
    time.sleep(1)  # задержка в 1 секунду между запусками
