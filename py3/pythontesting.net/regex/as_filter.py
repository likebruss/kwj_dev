import fileinput
import re

with fileinput.input(files='as_filter.txt') as f:
  for line in f:
    line = re.sub('foo', 'bar', line.rstrip())
    print(line)
