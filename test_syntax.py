# Tested with Python2 and Python3

import codecs

from uni_syntax import parser
from escapes import html

def test_syntax(file = 'tests/hierotestsuite.html'):
    f = codecs.open(file, encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        data = html.unescape(line)
        fragment = parser.parse(data)
        if fragment:
            if data == fragment.to_string():
                print('MATCH')
            else:
                print('NOT MATCH')
                print(data)
                print(fragment.to_string())

if __name__ == '__main__':
    test_syntax()
