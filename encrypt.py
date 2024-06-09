import random
import time
start = time.time()
s='0123456789abcdefghijklmnopqrstuvwxyz'
s2='abcdefghijklmnopqrstuvwxyz'
def min(a,b):
    if(a<b): return a
    return b
def chartoint(a):
    return s.find(a)
def inttochar(b):
    return s[b]
def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在。")
        return None
file_path = "m.txt"
file_content = read_txt_file(file_path)
def keep_letters_only(input_string):
    filtered_string = ''.join(filter(str.isalpha, input_string))
    return filtered_string
m=keep_letters_only(file_content).lower()
m=m*180#为快速得到大的明文以得到计算速度和更好的频率特性，直接将原来的明文重复180遍，新明文长度在10e5左右
mlen=len(m)
c=''
def read_file(file_path):
    keylist = []
    with open(file_path, 'r') as file:
        for line in file:
            keylist.append(line.strip())
    return keylist
file_path = "key.txt"
keylist = read_file(file_path)
keylenlist=[]
c2=''
for i in range(len(keylist)):
    keylenlist.append(len(keylist[i]))
i=0
while(i<mlen-1):
    j=random.randint(0,len(keylist)-1)
    c2+=inttochar(j)
    left=i
    right=min(i+keylenlist[j]-1,mlen-1)
    while(i<=right):
        a=keylist[j][i-left];
        x=(s2.find(a)+s2.find(m[i]))%26
        c+=s2[x]
        i+=1
c=c2+'-'+c
with open('c.txt', 'w') as file:
    file.write(c)
end = time.time()
print (str(end-start))
print(len(m))
print(len(c))