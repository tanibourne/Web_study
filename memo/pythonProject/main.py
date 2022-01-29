print('hello sparta!')

# 변수 자료형 함수 조건문 반복문

a = 7
b = 13
name = 'bk'

print(str(a)+name)

is_adult = True
is_fact = True

a_list = ["apple", "strawberry", "pear"]
print(a_list[2])
a_list.append("melon")
friends = ["철수", "영희"]
a_list.append(friends)
print(a_list)
print(a_list[4][1])

person = {'name': 'Bob', 'age': 18}

print(person)
print(person['name'])
a_list.append(person)
print(a_list)
print(a_list[5]['name'])

# def sum(c,d):
#     print('sum 안에서 인쇄합니다')
#     return c + d
#
# result = sum(1,5)
# print(result)

def sum(c, d):
    print('sum 안에서 인쇄')
    a + b

result = sum(1, 5)
print(result)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

# for person1 in people:
#     person1['addr'] = '역삼동'
#     print(person1)

def get_age(myname):
    for person1 in people:
        if person1['name'] == myname:
            return person1['age']
        return '모르는 이름입니다.'

print(get_age('bob'))
print(get_age('kay'))

ab = 'spartacodingclub@gmail.com'

def checkmail(mail):
    return mail.find('@') > -1

print(checkmail(ab))

def getmail(mail):
    return mail.split('@')[1].split('.')[0]

print(getmail(ab))

cnt_list = ['사과', '감', '감', '배', '포도', '포도', '딸기', '포도', '감', '수박', '딸기']

def count_list(v_list):
    result1 = { }
    for fruit in v_list:
        if fruit in result1:
            result1[fruit] += 1
        else:
            result1[fruit] = 1


    return result1
print(count_list(cnt_list))





