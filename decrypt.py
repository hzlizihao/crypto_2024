import time
start = time.time()
def min(a,b):
    if(a<b): return a
    return b
def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在。")
        return None
s2='abcdefghijklmnopqrstuvwxyz'
s='0123456789'+s2
file_path = "c.txt"
c = read_txt_file(file_path)
x=c.find('-')
c2=c[:x]
c=c[x+1:]
lenc=len(c)
m=''
def read_file(file_path):
    keylist = []
    with open(file_path, 'r') as file:
        for line in file:
            keylist.append(line.strip())  # 移除每行末尾的换行符并添加到列表中
    return keylist
file_path = "key.txt"  # 将文件路径替换为实际文件路径
keylist = read_file(file_path)
keylenlist=[]
for i in range(len(keylist)):
    keylenlist.append(len(keylist[i]))
i=0
for j in range(x):
    left=i
    b=s.find(c2[j])
    right=min(i+keylenlist[b]-1,lenc-1)
    while(i<=right):
        a=keylist[b][i-left]
        x=(s2.find(c[i])-s2.find(a))%26
        m+=s2[x]
        i+=1
with open('mnew.txt', 'w') as file:
    file.write(m)
end = time.time()
print (str(end-start))