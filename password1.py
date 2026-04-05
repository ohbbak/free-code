
import random

a_list=['a','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']

password_list=[]

ran=random.choice(a_list)
password_list.append(ran)

ran=random.choice(a_list)
password_list.append(ran)

ran=random.choice(a_list)
password_list.append(ran)


print(f"생성된 랜덤 비밀번호{password_list}")


