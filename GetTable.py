# 思路：输入字符串通过逗号或顿号统计项目数，然后根据艾宾浩斯记忆曲线规则生成最大n+15行、最少有5列（根据实际情况添加所需列）。
# 艾宾浩斯记忆曲线规则：今日学习，明日复习，后天复习，4天后复习，7天后复习，15天后复习
# 第一章程序设计基本方法,第二章Python语言基本语法元素,第三章基本数据类型,第四章程序的控制结构,第五章函数和代码复用,第六章组合数据类型,第七章文件和数据格式化,第八章Python计算生态,第九章Python标准库的概览,第十章Python第三方库概览,第十一章Python第三方库纵览
import openpyxl



def countChar(v_getchar):  # 统计项目个数
    return v_getchar.count(',') + v_getchar.count('、') + v_getchar.count('，')


def splitChar(v_getchar):  # 处理（统一）分隔符，入参字符串，返回列表
    v_getchar = v_getchar.replace('、', ',')
    v_getchar = v_getchar.replace('，', ',')
    v_getchar = v_getchar.split(',')
    return v_getchar


def getEbbinghausForgettingCurveTable(TableName, getCharList, countNumber):  # 获得最终表格
    EFCTable = list()
    EFCTable.append([TableName, '', '', '', '', '', '', ''])
    EFCTable.append(["天数", "日期", "记忆or学习", "复习1", "复习2", "复习3", "复习4", "复习5"])
    n = 1
    whileNumber = countNumber + 15
    while n <= whileNumber:

        # TemporaryList.clear()    #  清空列表会导致生成表格的内容也消失，就是会影响其他列表变量，所以这里使用列表重定义方法
        TemporaryList = list()  # 临时列表变量定义
        TemporaryList.append(n)  # 写入天数，顺序数
        TemporaryList.append('')  # 写入“日期”列空格行占位
        # 第一部分 学习 + 复习阶段
        if n <= countNumber:
            # for 项目循环获取
            forNumber = n - 1
            # getCharList[forNumber:]  --利用列表切片排序使今日学习项目第一个写入，以对齐表格
            for i in getCharList[forNumber:]:
                if n in i:
                    V_Char = ''.join(i[0:1])  # 列表元素转换为字符串
                    TemporaryList.append(V_Char)
            # getCharList[:forNumber] --补入列表切片之前的项目（已学习过项目写入复习列）
            for i in getCharList[:forNumber]:
                if n in i:
                    V_Char = ''.join(i[0:1])  # 列表元素转换为字符串
                    TemporaryList.append(V_Char)
        # 第二部分 纯复习阶段
        elif n > countNumber:
            # 增加记忆or学习行占位
            TemporaryList.append('')
            # for 项目循环获取
            for i in getCharList:
                if n in i:
                    V_Char = ''.join(i[0:1])  # 列表元素转换为字符串
                    TemporaryList.append(V_Char)
        # if 生产表格的空格占位写入
        if len(TemporaryList) < 8:

            V_Num = 8 - len(TemporaryList)
            while V_Num != 0:
                TemporaryList.append('')
                V_Num -= 1

        EFCTable.append(TemporaryList)
        n += 1
    return EFCTable


def main(v_char, TableName, PATH):
    countNumber = countChar(v_char) + 1  # 获得统计数
    splitCharList = []
    splitCharList = splitChar(v_char)  # 获得处理后的列表
    getCharList = list()
    n = 0
    for i in splitCharList:
        n += 1
        getCharList.append([i, n, n + 1, n + 2, n + 4, n + 7, n + 15])  # 循环计算每个项目会出现的位置
        if n == countNumber:  # 计算完所有项目后 退出循环
            break
    #TableName = input("输入表格名：")
    getTable = getEbbinghausForgettingCurveTable(TableName, getCharList, countNumber)

    #PATH = input("输入文件生成路径：")
    wb = openpyxl.Workbook()  # 生成excel表格
    ws = wb['Sheet']
    wb.remove(ws)  # 删除默认表格

    sheetName = TableName
    # sheetName = ''.join(getTable[0:1])  # 列表元素转换为字符串

    ws = wb.create_sheet(sheetName, None)  # 创建新的excel工作表
    # for 写入excel数据
    for i in getTable:
        FORLIST = list(i)
        ws.append(FORLIST)
    # 获得保存路劲+文件名
    PATH = PATH + sheetName + '.xlsx'
    # 保存excel表格
    wb.save(PATH)


#main()
