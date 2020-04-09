import random
import string
stringlen = 5
i = 0
p= 0

satisfied = 'y'
result = []

while satisfied.lower() == 'y':
    
    def passwordgen():
        rand='' .join(random.choice(string.ascii_letters) for i in range(stringlen))
        return f'{first_name[:2]}{last_name[-2:]}{rand}'

    first_name=input(f'''Please enter  first name for user {i+1}...  
''')

    last_name= input(f'''Please enter  last name for user {i+1}...
''')

    email= input(f'''Please enter email address for user {i+1}...
''')

    pword = passwordgen()
    # 
    password = input(f'''Would you like {pword} as your password? [Y/N]
''')
    if password.lower() == "y":
        password = pword
    elif password.lower() == "n":
        while len(password) < 7:
            password = input('''Please enter desired password...
''')
            if len(password)<7:
                print("Password must be at least 7 Characters")
            else:
                break
    result.append({})
    result[i]['fname'] = first_name
    result[i]['lname'] = last_name
    result[i]['email'] = email
    result[i]['password'] = password

    print(f'''
User {i} details: {result[i]}
    ''')
    i+=1
    satisfied = input('''Do you want to enter another user? [Y/N]
''')

if i>1:
    while p<i:
        print (f''' 
        {result[p]['email']}- {result[p]}''')
        p += 1
# print(password)
