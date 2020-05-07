from Parser.parser import parser
import logging
from click._compat import raw_input
import subprocess


# Read terminal
write = subprocess.Popen(["notepad","editor.txt"])
time = 0
print("waiting")
while write.poll() is None:
    time += 1
with open('editor.txt', 'r') as input:
    lines = input.readlines()
    textToAnalyze ='\t'.join([line.strip() for line in lines])
    print(textToAnalyze)

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
count = 0
while True:
    try:
        if count == 0:
            print('TESTING INPUT FILE')
            s = textToAnalyze
            count += 1
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s, debug=log)
    print(result)
    break
