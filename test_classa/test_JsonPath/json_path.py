# coding=UTF8





a={'shopId': 1, 'shopName': None, 'prodId': 4314, 'prodName': '多比安慕希商品名称', 'price': 0.01, 'content': '<p><img src="https://img30.360buyimg.com/sku/jfs/t1/96339/3/23283/167190/62199ea1Eba257ec8/85e0fdc226630736.jpg" alt="i1" width="1000" height="1144" /><img src="https://img30.360buyimg.com/sku/jfs/t1/95981/34/23619/211204/62199eb5E2121db72/a11dc35237d27e6f.jpg" alt="i2" width="1000" height="1263" /></p>', 'oriPrice': 0.01, 'waterSoldNum': 0, 'totalStocks': 1234, 'brief': '浓浓的超好喝', 'video': '', 'pic': 'http://mall.lemonban.com:8108/2022/10/0ec4569a5acd43b69bd7b9c4ef5553cb.png', 'imgs': 'http://mall.lemonban.com:8108/2022/10/0ec4569a5acd43b69bd7b9c4ef5553cb.png', 'categoryId': 290, 'prodType': 0, 'scorePrice': None, 'liveRoomParams': [], 'skuList': [{'skuId': 4765, 'price': 0.01, 'oriPrice': 0.01, 'stocks': 2, 'skuName': '白色 ', 'skuScore': 1, 'pic': None, 'properties': '颜色:白色'}, {'skuId': 11581, 'price': 0.01, 'oriPrice': 0.01, 'stocks': 1234, 'skuName': '', 'skuScore': 1, 'pic': None, 'properties': ''}], 'groupActivityId': 0, 'activityPrice': None, 'startDeliveryFee': None, 'deliveryModeVO': {'hasUserPickUp': False, 'hasShopDelivery': True, 'hasCityDelivery': False}, 'preSellStatus': 0, 'preSellTime': None}


#根目录 /  $   .

#jsonpath  一个.  表示下一个层级    ..表示所有子孙层级   一些模块不要用命名
# print(a['skuList'][0]['skuId'])
import jsonpath
print(jsonpath.jsonpath(a,'$..skuId')[0])  #如果里面skuid有多个值，再根据切片取值自己想要的

