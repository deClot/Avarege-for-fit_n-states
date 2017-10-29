import os

TRANS_path = os.path.abspath('TRANS.RES')
res_path = os.path.abspath ('res.res')

if os.path.exists(TRANS_path)==False:
    TRANS_path =os.path.abspath('Avarege_for_fit_n_states/TRANS.RES')
    res_path = os.path.abspath('Avarege_for_fit_n_states/res.res')


while(True):
    f=open(TRANS_path, 'r').readlines()
    l=len(f)

    if f[l-1].find('J=',0,len(f[l-1]))==-1:
        f.pop(-1)
        with open(TRANS_path,'w') as F:
            F.writelines(f)
    else:
        break

file = open(TRANS_path, 'r')
file2 = open(res_path,'w')
while (True):
    str1=file.readline()
    if len (str1)==0:
        break

    if str1.find ('iteration',0,len(str1))!=-1:
        t=file.tell ()

file.seek (t,0)
while(True):
    str1=file.readline()
    if str1.find ('matrix',0,len(str1))!=-1: #sodershit matrix
        break

for line in file:
    file2.write (line)
    
file.close()
