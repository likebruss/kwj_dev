import fileinput
import re

for line in fileinput.input(files='as_filter.txt', inplace=1, backup='.bak'):
  line = re.sub('foo', 'bar', line.rstrip())
  print(line)
