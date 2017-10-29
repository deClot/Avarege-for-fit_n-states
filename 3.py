#########################

def clearning_string (str1):
    str1=str1[0:79]
    str1=str1.replace('+',' ')
    str1=str1.replace('-',' ')
    str1=str1.replace('p',' ')
    str1=str1.replace('?',' ')
    str1=str1.replace('_',' ')

    return str1
##########################

import os

init_path = os.path.abspath('avarege for fit_n')
second_path = os.path.abspath('res2.res')
res_path =  os.path.abspath('Result_avarege of fit_n.txt')


if os.path.exists(init_path)==False:
    init_path =os.path.abspath('Avarege_for_fit_n_states/avarege for fit_n')
    second_path = os.path.abspath('Avarege_for_fit_n_states/res2.res')
    res_path = os.path.abspath('Avarege_for_fit_n_states/Result_avarege of fit_n.txt')


    #file3=open(second_path, 'r')
file=open (init_path, 'r')
file2=open (res_path, 'w')

#file=open ('avarege for fit_n', 'r')
#file2=open ('Result_avarege of fit_n.txt', 'w')

print ('State')
vv=input()

b=0
list1=[]
while (True):
    if b==1:
        break
    while (True):
        str1=file.readline()
        if len(str1) == 0: # Нулевая длина обозначает конец файла (EOF)
            b=1
            break
        else:
            b=0
        if str1.find ('Search',0,len(str1))!=-1: #sodershit matrix
            list1=[]
            str1=clearning_string(str1)
            str1=str1.split()
            J=str1[1]
            ka=str1[2]
            kc=str1[3]
            a=0
            file3=open(second_path, 'r')
            for str3 in file3:
                #if str3.find ('matrix',0,len(str3))!=-1: #sodershit matrix
                    #continue
                #else: 
                        str3=str3.replace ('J=','')
                        str3=str3.split()
                        #print (str3[3],str3[4],str3[5])
                        if str3[2]==vv and str3[3]==J and str3[4]==ka \
                           and str3[5]==kc:
                            v=str3[0]
                            break
            file3.close()
        else:
            str1=clearning_string(str1)
            str1=str1.split()

            if len(str1)>=12:
                list1.append(float(str1[5]))
                list1.append(float(str1[11]))
                tell=file.tell()
                #print('tell=',tell)
            else:
                #if len(str1)>=6 and len(str1)<12:
                if len(str1)==6:
                    if len(str1)==6:
                        list1.append(float(str1[5]))
                    else:
                        list1.append(float(str1[6]))
                    tell=file.tell()
                    #print('tell=',tell)
                else:
                    tell=file.tell()
                    #print('tell=',tell)
                    
            
            tell=file.tell()
            #print('!',str1)
            str1=file.readline()
            #print('!!',str1)
            if str1.find('Search',0,len(str1))!=-1 or len(str1) == 0:
                #print('len=',len(list1), list1)
                avarage=0
                for i in range(len(list1)):
                    avarage=avarage+list1[i]
                    print (avarage, list1[i])
                avarage=avarage/len(list1)

                print ('----------------')
                #print (J,ka,kc)
                print ('av.=',avarage)
                file2.write('%5s %11.5f   100%5s%3s%3s\n' %(v,avarage,J,ka,kc))
                file.seek(tell)
            else:
                file.seek(tell)

a=input ()

file.close()
file2.close()
