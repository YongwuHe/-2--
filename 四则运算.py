import random
from tkinter import *
from tkinter import messagebox

a=[]
b=[]
c=[]
fuhao=[]
pos=[]
aa=[]
bb=[]
cc=[]
fu=[]
hao=[]
aans=[]

def main():
    n=int(Et1.get());
    pos.clear();
    a.clear();b.clear();c.clear();
    aa.clear();bb.clear();cc.clear();fu.clear();hao.clear();aans.clear();
    Te1.delete(1.0,END)
    count=0;
    for i in range(0,9999999):
        a.append(random.randint(0,99));
        b.append(random.randint(0,99));
        c.append(random.randint(0,99));
        fuhao.clear()
        if count==n: break;
        for j in range(0,2):
            k=random.randint(0,3);
            if(k==0):
                fuhao.append('+');
            elif(k==1):
                fuhao.append('-');
            elif(k==2):
                fuhao.append('x');
            elif(k==3):
                fuhao.append('/');
        if((fuhao[0]=='/' and b[i]==0)or (fuhao[1]=='/' and c[i]==0)):
            i=i-1;
            continue;
        else:
            if(fuhao[0]=='+'):
                if(fuhao[1]=='+'):
                    ans=a[i]+b[i]+c[i];
                elif(fuhao[1]=='-'):
                    ans=a[i]+b[i]-c[i];
                elif(fuhao[1]=='x'):
                    ans=a[i]+b[i]*c[i];
                else:
                    num=random.randint(1,10);
                    b[i]=num*c[i];
                    if(b[i]>100):
                        i=i-1;
                        continue;
                    ans=a[i]+b[i]/c[i];
            elif(fuhao[0]=='-'):
                if(fuhao[1]=='+'):
                    ans=a[i]-b[i]+c[i];
                elif(fuhao[1]=='-'):
                    ans=a[i]-b[i]-c[i];
                elif(fuhao[1]=='x'):
                    ans=a[i]-b[i]*c[i];
                else:
                    num=random.randint(1,10);
                    b[i]=num*c[i];
                    if(b[i]>100):
                        i=i-1;
                        continue;
                    ans=a[i]-b[i]/c[i];
            elif(fuhao[0]=='x'):
                if(fuhao[1]=='+'):
                    ans=a[i]*b[i]+c[i];
                elif(fuhao[1]=='-'):
                    ans=a[i]*b[i]-c[i];
                elif(fuhao[1]=='x'):
                    ans=a[i]*b[i]*c[i];
                else:
                    num=random.randint(1,10);
                    b[i]=num*c[i];
                    if(b[i]>100):
                        i=i-1;
                        continue;
                    ans=a[i]*b[i]/c[i];
            else:      
                a[i]=2*b[i];
                if(a[i]>100):
                    i=i-1;
                    continue;
                if(fuhao[1]=='+'):
                    ans=a[i]/b[i]+c[i];
                elif(fuhao[1]=='-'):
                    ans=a[i]/b[i]-c[i];
                elif(fuhao[1]=='x'):
                    ans=a[i]/b[i]*c[i];
                else:
                    i=i-1;
                    continue;
            if(a[i]>100 or b[i]>100 or c[i]>100):
                i=i-1;
                continue;
            if(ans<0 or ans>100):
                i=i-1;
                continue;
            else:
                count+=1;
                pos.append(i);
                aa.append(a[i]);
                bb.append(b[i]);
                cc.append(c[i]);
                fu.append(fuhao[0]);
                hao.append(fuhao[1]);
                aans.append(ans);
    output();
def output():
    n=int(Et1.get());
    Te1.delete(1.0,END)
    for i in range(0,n):
        if(CheckVar.get()==1):
            Te1.insert(INSERT,"%-2d%c%-2d%c%-2d = %-2d      "%(aa[i],fu[i],bb[i],hao[i],cc[i],aans[i]));
            if(i%2==1):
                Te1.insert(INSERT,"\n");
        else:
            Te1.insert(INSERT,"%-2d%c%-2d%c%-2d =      "%(aa[i],fu[i],bb[i],hao[i],cc[i]));
            if(i%2==1):
                Te1.insert(INSERT,"\n");
            
def export():
    fp=open("./四则运算题目.txt","w")
    n=int(Et1.get());
    Te1.delete(1.0,END)
    for i in range(0,n):
        if(CheckVar.get()==1):
            fp.write("%-2d%c%-2d%c%-2d = %-2d      "%(aa[i],fu[i],bb[i],hao[i],cc[i],aans[i]));
            if(i%2==1):
                fp.write("\n");
        else:
            fp.write("%-2d%c%-2d%c%-2d =      "%(aa[i],fu[i],bb[i],hao[i],cc[i]));
            if(i%2==1):
                fp.write("\n");
    fp.close()

root = Tk(className="四则运算器")
root.geometry("300x400")
root.resizable(0,0)


frame_root=Frame(root)
frame_root.pack()
frame1=Frame(frame_root)
frame1.pack()
frame2=Frame(frame_root)
frame2.pack()

Lb1=Label(frame1,text="题目数量",bd=10,font=("Arial",12),width=5,height=1)
Et1=Entry(frame1,width=5)
Bt1=Button(frame1,text="确定",activebackground='blue',command=main)
CheckVar=IntVar()
Ck1=Checkbutton(frame1,text="显示答案",command=output,variable=CheckVar)
Bt2=Button(frame1,text="导出",command=export)
Sc=Scrollbar(frame2)
Sc.pack(side=RIGHT,fill=Y)
Te1=Text(frame2,height=50,yscrollcommand=Sc.set)
Sc.config(command=Te1.yview)

Lb1.pack(side=LEFT)
Et1.pack(side=LEFT)
Bt1.pack(side=LEFT)
Bt2.pack(side=LEFT)
Ck1.pack(side=LEFT)
Te1.pack()
root.mainloop() 
