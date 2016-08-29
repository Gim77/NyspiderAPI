# NyspiderAPI

#####1.IT桔子
```python
from spider.itjuzi import *

inves=investevents(page=1)#国内投资信息

mergerdata=merger(pahe=1)#国内并购信息

foreignInves=foreign_investevents(page=1)#国外投资信息

foreignMergerdata=foreign_merger(page=1)#国外并购信息

```

#####2.拉勾网职位信息
```python
from spider.lagou import *

jobs=lagouJobs(page=1,keyword='')#拉勾网职位信息

```

#####3.猫眼电影
```python
from spider.maoyan import *

data=boxoffice(day='2016-05-03')#电影票房

movie=movieinfor(url='http://piaofang.maoyan.com/movie/247575?_v_=yes')#电影具体信息

```

#####4.人人贷散标信息
```python
from spider.renrendai import *

username='Your username'
passwd='xxx'#加密后的密码

work=Renrendai(username,passwd)
loaninfor=work.getLoan(loanid=80000)#获取散标数据

```
#####5.安居客
```python
from spider.anjuke import *

community('http://beijing.anjuke.com/community/p2/')#小区信息\

hourse=newHourse('http://bj.fang.anjuke.com/?from=navigation')#新房信息

```

#####6.大众点评
```python
from spider.dianping import *

result=bestRestaurant(cityId=1,rankType='popscore')#获取人气餐厅

shoplist=dpindex(cityId=1,page=1)#商户风云榜

restaurantlist=restaurantList('http://www.dianping.com/search/category/2/10/p2')#获取餐厅

```

#####7.获取代理IP
爬取http://proxy.ipcn.org，获取可用代理
```python
from spider.proxyip import get_enableips

enableips=get_enableips()

```

#####8.中国联通查询
```python

from spider.chinaunicom import *
user='18500000000'#phonenumber
passwd='000000'#服务密码
unicom=Unicom(user,passwd)
unicom.query_realtimefee()#查询实时话费
unicom.query_package()#查询套餐余量

```

#####9.百度地图
百度地图提供的API,对查询有一些限制，这里找出了web上查询的接口
```python
from spider.baidumap import *

citys=citys()#获取城市列表
result=search(keyword="美食",citycode="257",page=1)#获取搜索结果

```
