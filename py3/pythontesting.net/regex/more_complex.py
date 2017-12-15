import fileinput
import re

for line in fileinput.input(files='more_complex.txt'):
  line = re.sub(r'\* \[(.*)\]\(#(.*)\)', r'<h2 id="\2">\1</h2>', line.rstrip())
  print(line)
