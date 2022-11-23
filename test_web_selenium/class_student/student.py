

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
def ii():
    k = PyKeyboard()
    m = PyMouse()
    filepath = '/'
    k.press_keys(['Command', 'Shift', 'G'])
    x_dim, y_dim = m.screen_size()
    m.click(x_dim // 2, y_dim // 2, 1)
    # 复制文件路径开头的斜杠/
    pyperclip.copy(filepath)
    # 粘贴斜杠/
    k.press_keys(['Command', 'V'])
    # 输入文件全路径进去
    k.type_string(config.thing_file)
    k.press_key('Return')
    time.sleep(2)
    k.press_key('Return')
    time.sleep(2)