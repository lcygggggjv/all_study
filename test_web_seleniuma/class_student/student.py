

class ActionChains:

    # def __init__(self,driver):
    #
    #     self.driver=driver

    def click(self):

        print("点击")

    def send_keys(self):

        print("发送")



def perform():
    lst = ['click', 'send_keys']
    for l in lst:
        #不用函数 method=getattr(ActionChains(),’l‘)
        method=getattr(ActionChains(),l)    #取列表的字符串的名称，通过getattr找act的，对应方法名称
        method()  #method可以直接调用


perform()