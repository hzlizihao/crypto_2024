from collections import Counter
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
list1=[0]*26;list2=[];list3=[]
for i in range(len(c)):
    list1[s2.find(c[i])]+=1
    if(i==len(c)-1):
        break
    pair2=c[i:i+2]
    list2.append(pair2)
    if (i==len(c)-2):
        break
    pair3 = c[i:i+3]
    list3.append(pair3)
for i in range(26):
    print(s2[i],":",round(list1[i]/len(c),5))
list2_counter = Counter(list2)
list2top10=list2_counter.most_common(10)
for pair, frequency in list2top10:
    print(f"{pair}: {frequency}")
list3_counter = Counter(list3)
list3top10=list3_counter.most_common(10)
for pair, frequency in list3top10:
    print(f"{pair}: {frequency}")
keynumlist=[0]*36
for i in c2:
    keynumlist[s.find(i)]+=1
print(keynumlist)