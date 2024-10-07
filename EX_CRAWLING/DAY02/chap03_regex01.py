import re

m = re.match('[a-z]+','Python')
print(m)
print(re.search('apple','I like apple!'))

p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

m= re.match('[a-z]+','pythoN')
print(m)

m=re.match('[a-z]+','PYthon')
print(m)

print(re.match('[a-z]+','regex python'))

# findall()함수
# - 일치하는 모든 물자열을 리스트로 리턴
p = re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

# search() 함수
# 일치하는 첫 번째 문자열만 리턴

result = p.search('I like apple 123')
print(result)

result = p.findall('I like apple 123')
print(result)

# Match 메소드 예제 (전화번호 분석)
import re
tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')

print(tel_checker.match('02-123-4567'))
match_groups = tel_checker.match('02-123-4567').group()
match_groups = tel_checker.match('02-123-4567').groups()
print(match_groups)

print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))
## - dash(-) 제거하고 검사하기
tel_number = '053-950-4567'
tel_number = tel_number.replace('-','')
print(tel_number)

tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))

tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')
m = tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ',m.group())
print('group(0): ',m.group(0))
print('group(1): ',m.group(1))
print('group(2,3): ',m.group(2,3))
print('start(): ',m.start())
print('end(): ',m.end())
print('span(): ',m.span())

cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))

# 전방 탐색(lookahead)
lookahead1 = re.search('.+(?=won)','1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')
lookahead2 = re.search('.+(?=am)','2023-01-26 am 10:00:01')
print(lookahead2.group())

lookahead3 = re.search('\d{4}(?!-)','010-1234-5678')
print(lookahead3)

# 후방 탐색(lookbehind)
lookbehind1 = re.search('(?<=am).+','2023-01-26 am 11:10:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+','USD: $51')
print(lookbehind2)

lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apple')
print(lookbehind4)
