#알파벳 소문자, 숫자 3글자를 랜덤 선택하여 패스워드를 생성하는 프로그램
#a_list로 하고 ['a','b','c'... random.choice(a_list)]
import random

a_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']

password_list=[]

ran=random.choice(a_list)
password_list.append(ran)

ran=random.choice(a_list)
password_list.append(ran)

ran=random.choice(a_list)
password_list.append(ran)


print(f"생성된 랜덤 비밀번호{password_list}")


