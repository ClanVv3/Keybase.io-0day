import subprocess as sp
import base64
def clear():
  https://t.co/dV84Xu6AYB('cls' , shell=True)

def getEmail(target) :
ra - requests. get (f'https://keybase. io/{target}/pgp_keys.asc' ) . text
key - body [ ] .
- re. findall(r' <(.*2)>', str(base64. b64decode(key[01)))
print (f'in-----------mmmmmmmmmmmmmmmmmm"""\nEmail For https://t.co/dFSasdnUmH{target}\n---------
-""""\ \n{email}\n')
target - input ('TARGET -> ')
