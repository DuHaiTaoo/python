#-*-coding:utf-8;-*-



import random #用于取随机数
import platform 
import os

#---------------定义函数---------------------



def number():
    print("-" * 20)
    a = input ("请输入要猜的数字位数\n")
    if len(a) == 0:
        number ()
        return "0"
    #if (int(a) < 3 or int(a) > 6):
    if (int(a) < 1):
        print("-" * 20)
        print("输入错误，看起来{0}不是一个正确的选择！".format(a))
        number ()
    else:
        return str(a)

def repeat():
    print("-" * 20)
    #print("请选择是否有出现重复的数字(不一定)")
    #print("   y 是    n 否")
    a = input("请选择是否有出现重复的数字(不一定)\n   y 是    n 否\n")
    if len(a) == 0:
        repeat ()
        return
    print("-" * 20)
    if a == "y":
        print("您选择了出现重复的数字。")
        return "y"
    elif a == "n":
        print("您选择了不出现重复的数字。")
        return "n"
    else:
        
        print("输入错误，" + str(a) + "不是一个正确的选择！")
        return repeat ()


def make(number,repeat):
    print("-" * 20)
    if repeat == "y":
        print("您当前的选择是{0}位数，会出现重复的数字".format(number))
    else :
        print("您当前的选择是{0}位数，不会出现重复的数字".format(number))
    print("生成中...")
    a = []
    
    if repeat == "y":
        for i in range(int(number)):
            a.append( str(random.randint(0,9)))
    else:
        b = list(range(0,9))
        a = random.sample(b,int(number))
        a = [str(i) for i in a]
        
    answer = "".join(a)
    print("答案是" + answer)
    return answer
    
def guess(answer,number,repeat,time):
    
    #print(time)
    print("-" * 20)
    a = list(input("请输入您第{0}次猜测的{1}位数字\n".format(time,number)))
    b = list(answer)
    
    A = B = 0
    
    if(len(a) != len(b)):
        print("输入错误，请重新输入!")
        guess (answer,number,repeat,time)

    c = []
    
    for i in range(int(number)):

        if (a[i] == b[i]):
            A = A + 1
            c.append(i)       

    for i in range(int(number)):
        d = range(int(number))
        d = list(d)
        for n in c:
            d.remove(n)
    
    
    for i in d:
        for n in d:
            if a[i] == b[n] and i != n:
                B = B+1
                break
            
    #print(d)
    



    print("{0}A{1}B".format(A,B))
    if(A != int(number)):
        guess (answer,number,repeat,time + 1)
    else:
        print("-" * 20)
        print("\n恭喜您猜对了！！！\n")
        print("-" * 20)
        print("请选择是否再来一局\n  y 重来 n 退出")
        c = input ()
        if (c == "n"):
            exit()
        if (c == "y"):
            ColdMo ()


def ColdMo ():
    _number = number()
    _repeat = repeat()
    _answer = make(_number,_repeat)
    guess (_answer,_number,_repeat,1)



if __name__ == "__main__":

    
    
    print("-" * 20)
    print("\n欢迎来到猜数字！！！\n   By:Cold-mo\n")
    
    _number = number()
    _repeat = repeat()
    _answer = make(_number,_repeat)
    guess (_answer,_number,_repeat,1)
    
    
