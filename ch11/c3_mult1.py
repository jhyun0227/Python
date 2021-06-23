import re
p = re.compile("^python\s\w+", re.MULTILINE) # re.MULTILINE 여러줄 확인
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))