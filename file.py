# %%
"""
1. 텍스트 파일 쓰기
"""

# %%
# 파일 경로
file_name = '/content/example.txt'
try :
  # 파일을 쓰기모드로 열기
  file = open(file_name, 'w')
except FileNotFoundError as e:
  print('파일이 존재하지 않습니다.')
else :
  # 파일에 쓰기
  file.write('hello, world!')
finally :
  # 자원반납
  file.close()

# %%
"""
2. 텍스트 파일 읽기
"""

# %%
file_name = '/content/example.txt'
try :
  file = open(file_name, 'r')
except FileNotFoundError as e:
  print('파일이 존재하지 않습니다.')
else :
  text = file.read()
  print(text)
finally :
  file.close()

# %%
"""
3. 파일에 여러 줄 쓰기
"""

# %%
file_name = '/content/example.txt'

lines = [
    "Hello, world1!",
    "Hello, world2!",
    "Hello, world3!"
]

# with문은 close 메소드 호출이 필요 없다
with open(file_name, 'w') as file :
  for line in lines :
    file.write(line)
    file.write('\n')  # 줄바꿈

# %%
"""
4. 파일에 추가하기
"""

# %%
file_name = '/content/example2.txt'

lines = [
    "Hello, world4!",
    "Hello, world5!",
    "Hello, world6!"
]

# 파일이 존재하면 추가, 파일이 존재하지 않으면 신규파일을 생성하고 쓰기작업
with open(file_name, 'a') as file :
  for line in lines :
    file.write(line)
    file.write('\n')

# %%
"""
5. JSON 포맷 문자열을 파일에 저장하기
"""

# %%
import json

# dic = {}
dic = dict()
dic['person'] = '사람'
dic['student'] = '학생'
# print(dic)

# dir(json)
# json.dumps?
# help(json.dumps)
dict_json_str = json.dumps(dic, ensure_ascii=False, indent=4)

file_name = '/content/example3.txt'
with open(file_name, 'a') as file :
  file.write(dict_json_str)


# %%
"""
6. JSON 포맷 문자열이 저장된 파일을 읽어 딕셔너리 객체에 저장하기
"""

# %%
file_name = '/content/example3.txt'
with open(file_name, 'r', encoding='utf-8') as file :
  data_dict = json.load(file) # json포맷 문자열 => 딕셔너리로 변환

print(type(data_dict))
print(data_dict['person'])
print(data_dict)


# %%


# %%
