import os,sys
print("欢迎使用uncode")
print("请开始输入")
step = []
tab = 0
step.append("start")
while True:
    text = input("")
    if "if:" in text  or "while:" in text:
        step.append('   '*tab+text)
        tab = tab + 1
    else:
        step.append('   '*tab+text)
    if ':wq' in text:
        end = len(step)-1
        step.remove(step[end])
        try:
            file = open('.\\save\\'+ text[4:] +'.uncode','r')
            print("存在文件是否要覆盖(y or n): ",end='')
            choose = input()
            if choose == 'y' or choose == 'Y':
                file = open('.\\save\\'+ text[4:] +'.uncode','w')
            elif choose == 'n' or choose == 'N':
                print("请重新输入文件名",end='')
                fileName = input()
                file = open('.\\save\\'+ fileName +'.uncode','w')
        except FileNotFoundError:
            file = open('.\\save\\'+text[4:]+'.uncode','w')
            for i in step:
                file.write(i+'\n')
        break