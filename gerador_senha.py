import random
import string

def geraSenha():
    
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(8))

for i in range(4):
    print ("Random String is ", geraSenha() )
