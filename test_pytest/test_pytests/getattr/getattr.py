



class A:

    def fixt(self):

        return 'hello'


#用fixt  保存这个fixt的属性
fixt='fixt'

a=getattr(A(),fixt)
#通过getattr 调用A类的，fixt属性

#再用fixt 保存传进去
fixt=a()
print(fixt)
