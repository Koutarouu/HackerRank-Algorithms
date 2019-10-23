import re

n=[]
for _ in range(int(input())):
    firstName, emailID = input().split()
    if len(firstName)>20: raise ValueError
    if len(emailID)>50: raise ValueError
    if not bool(re.match(r"[a-z]*", firstName)): raise ValueError
    if not bool(re.match(r"[a-z]|\.+@+\w+\.+\w", emailID)): raise ValueError
    if emailID.split('@')[1] == 'gmail.com':
    	n.append(firstName)
print(*sorted(n), sep='\n')


"""
Each of the first names consists of lower case letters [a-z] only.
Each of the email IDs consists of lower case letters [a-z],@ and . only.
The length of the first name is no longer than 20.
The length of the email ID is no longer than 50.
hola.hola@gmail.com
"""