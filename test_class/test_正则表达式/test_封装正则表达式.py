
import re


class Data:  # 把数据的类，写到函数里面
    smsflag =''
    mobile = ''
    username = ''

def replace_data(string,pattern='#(.+?)#'):
    ##数据替换

    # class Data:   #把数据的类，写到函数里面
    #     smsflag = ''
    #     mobile = ''
    #     username = ''

    #找出所有的   #（）#    #.?#做成参数，给个默认值，如果改变格式吗，直接输入即可
    result=re.finditer(pattern,string)  #finditer  取全部

    for el in result:
        old=el.group()   #找出老的数据

        new_name =el.group(1)  #数组第一个
        # new_name=old.strip('#')  #去除两边的#号，等于

        new_=getattr(Data,new_name)  #等于  类里的 data.new_name
        string=string.replace(old,new_)  #替换，前面旧数据，后面新数据

    return string

if __name__ == '__main__':

    replace_smsflag='asdf'
    mobile='15677778888'   #要准备新的数据
    res=replace_data('{"name":"#smsflag#","age":"12","mobile":"#mobile#"}')   #准备好旧的数据，替换要是字符串最外层

    print(res)


