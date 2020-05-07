from Parser.parser import parser
import logging
import subprocess


# Read terminal
write = subprocess.Popen(["notepad","editor.txt"])
time = 0
print("waiting")
while write.poll() is None:
    time += 1
# Read document and convert all commands into a single line
with open('editor.txt', 'r') as input:
    lines = input.readlines()
    textToAnalyze ='\t'.join([line.strip() for line in lines])
    print(textToAnalyze)
# Set up debugger for parser
logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()
count = 0
# Process file
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
    print('FINISHED PROCESSING INPUT FILE')
    break
