import re
match1 = re.match('[0-9]','1234')
print(match1.group())
match1 = re.match('[0-9]','abcd')
print(match1)
#print(match.group()), match 되는 것이 하나도 없다, match되는 것이 하나도 없으면 group 사용할 수 없다.
match1 = re.match('[0-9]+','1234') # +는 1개 이상
print(match1)
print(match1.group())