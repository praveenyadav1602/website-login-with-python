import requests

class bcolors:
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


print (bcolors.UNDERLINE+"                                                                       ")
print ("***********************************************************************")
print ("***********************************************************************"+ bcolors.ENDC)
print ("                    script created by praveen yadav                    ")
print (bcolors.UNDERLINE+"***********************************************************************")
print ("***********************************************************************"+ bcolors.ENDC)

print('\n')



url= 'https://askubuntu.com/users/login?ssrc=head&returnurl=https%3a%2f%2faskubuntu.com%2f'
EMAIL = input("ENTER YOUR EMAIL ADDRESS\n")
PASSWORD = input("ENTER YOUR PASSWORD\n")
data = {'email':EMAIL,'ssrc':'head','password':PASSWORD,'fkey':''}
login = requests.post(url, data = data)
content = login.text
print (login.status_code)
with open('index.html', 'w') as file:
    file.write(content)
if 'logout' in content:
    print ("login success")
else:
    print("login failed")


print("index.html page saved")
