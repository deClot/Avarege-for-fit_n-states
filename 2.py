import os

res_path =  os.path.abspath('res.res')
res2_path = os.path.abspath('res2.res')

#if os.path.exists(res_path)==False:
#    res_path = os.path.abspath('Avarege_for_fit_n_states//res.res')
#    res2_path = os.path.abspath('Avarege_for_fit_n_states/res2.res')

file=open (res_path, 'r')
file2=open(res2_path,'w')

def func (v,v0,list1,str3,list2,no,E2):
    if v==v0:
        list1.append(str3)
        k=[E2,no]
        list2.append(k)
    else:
        def sort_col(i):
            return i[0]
        #print (list2)
        list2.sort(key=sort_col)
        #print (list2)
        #a=input ()
        v0=v
        for i in range(len(list2)):
            file2.write('%5s V=%2s  J=%2s%3s%3s'%(list2[i][1],\
                        list1[i][2],list1[i][3],list1[i][4],list1[i][5]))
            if len(list1[i])==6:
                file2.write('%34s\n'%(list2[i][0]))
            if len(list1[i])==7:
                file2.write('%17s%17s\n'%(list1[i][6],list2[i][0]))
        
        list1=[]
        list2=[]
        
        list1.append(str3)
        k=[E2,no]
        list2.append(k)


    return v0,list1,list2
    

b=0
list1=[]
list2=[]

v0=1

"""str1=file.readline()
str1=str1.split()
v1,*_=str1
v1=int (v1)

str1=file.readline()

for i in range((v1**2)*6+1):
    str1=file.readline()
"""
while (True):
    str1=file.readline() 
    str2=str1[0:55]
   
    if len(str2)==0:
       break

    if str2.find ('matrix',0,len(str1))!=-1: #sodershit matrix
        continue
    str2=str2.replace ('J=','')
    str2=str2.split()
    if len(str2)==7:
        no,_,v,J,Ka,Kc,E2=str2
        E2 = float(E2)
        str3=no,_,v,J,Ka,Kc
        v=int(v)
        kk,list1,list2=func (v,v0,list1,str3,list2,no,E2)
        v0=kk
    if len(str2)==8:
        no,_,v,J,Ka,Kc,E1,E2=str2
        E2 = float(E2)
        str3=no,_,v,J,Ka,Kc,E1
        v=int(v)
        kk,list1,list2=func (v,v0,list1,str3,list2,no,E2)
        v0=kk
        continue
#    str2=str2.replace ('J=','')
#    str2=str2.split()


    

file.close()
file2.close()
