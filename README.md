# FirstPython
0. douban包，用来爬豆瓣书单的，ex:豆瓣top 250, 或者根据书单的tag爬
1. 环境:window7 64，Python2.7, PyCharm， mysql， redis
2. 保存微博用户信息这里用redis保存，使用redis的key value特性，使用hash对象对象保存微博用户信息.使用user:uid作为主键，其他属性key-value保存
    ex:
    uid = 5905555624
    user:5905555624 uid 5905555624 nickname 小北帅三代

3. 遍历使用DFS，每次使用一个种子UID，并加入到使用过的uid中，遍历关注者中的uid，选择种子uid(遍历已使用过的uid进行去重)
4. 使用user-agent池，伪装客户端请求(后期可以考虑使用cookie伪装数据库)
