


class page:


    def click(self):
        print('点击')

    def send_keys(self):
        print('输入')

    def get_url(self):
        print('输入')



pages=page() #初始化
pages.click()  #调用

action=input('输入操作：')

if action in ['click','send_keys','get_url']:

    method=getattr(pages,action)
    print(method)
    method()
else:
    print('ww')

