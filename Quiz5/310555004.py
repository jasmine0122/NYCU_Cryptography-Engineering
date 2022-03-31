import hashlib
import secrets
#c606196ea460a3a53ac3e81c614b990b //example1
#0228e3b50cd30ee5084bfb7340fd5a2d //example2 

def hash(s):
    data = hashlib.md5(s)
    return data.hexdigest()

def collision(msb):
    m = str();
    while(m[:4] != msb):
        t2 = secrets.token_hex(16)
        m = hash(bytes.fromhex(t2));
        if (m[:4] == msb):
            return t2

t = input('')
h = hash(bytes.fromhex(t));
print(h[:4], end=' ') #The 16 MSB of the MD5 in hexadecimal 
print(collision(h[:4]))
