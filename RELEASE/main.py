import release_parser
import logging
import subprocess

real_parser = release_parser.release_parser
# Read terminal
write = subprocess.Popen(["notepad", "editor.txt"])
time = 0
print("waiting")
while write.poll() is None:
    time += 1
# Read document and convert all commands into a single line
with open('editor.txt', 'r') as input:
    lines = input.readlines()
    textToAnalyze = '\t'.join([line.strip() for line in lines])
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
    result = real_parser.parse(s, debug=log)
    print(result)
    print('FINISHED PROCESSING INPUT FILE')
    break

with open('OUTPUT.txt', 'w') as output:
    for line in release_parser.messages:
        output.write(str(line))
        output.write("\n")
subprocess.Popen(["notepad", "OUTPUT.txt"])
