import sys

# 初始化变量
step = []  # 存储每一步的代码
tab = 0  # 缩进级别
tabs = []  # 存储每一步的缩进级别
position = 0  # 当前位置

print("欢迎使用noncode")
print("请开始输入")

# 添加起始步骤
step.append("start")
while True:
    text = input("")

    # 处理命令
    if ':back' in text:  # 回退命令
        try:
            position = position + int(text[5:])
        except ValueError:
            position = position + 1
        finally:
            continue
    elif ':wq' in text:  # 保存并退出命令
        end = len(step)-1
        step.remove(step[end])
        try:
            file = open('.\\save\\'+ text[4:] +'.noncode','r')
            print("存在文件是否要覆盖(y or n): ",end='')
            choose = input()
            if choose == 'y' or choose == 'Y':
                file = open('.\\save\\'+ text[4:] +'.noncode','w')
            elif choose == 'n' or choose == 'N':
                print("请重新输入文件名",end='')
                fileName = input()
                file = open('.\\save\\'+ fileName +'.noncode','w')
        except FileNotFoundError:
            file = open('.\\save\\'+text[4:]+'.noncode','w')
            for i in step:
                file.write(i+'\n')
        break

    # 检查输入
    if position >= 1:  # 替换指定位置的代码
        needChangePosition  = len(step) - position
        step[needChangePosition] = '    '*tabs[needChangePosition-1]+text
        position = 0
    elif "if:" in text  or "while:" in text:  # 处理if和while语句
        step.append('   '*tab+text)
        tabs.append(tab)
        tab = tab + 1
    else:  # 添加普通代码
        step.append('   '*tab+text)
        tabs.append(tab)