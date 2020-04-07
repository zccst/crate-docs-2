DEX Operations Guide (CLI)
==============================

This document contains all the necessary information for DEX operations to interact with the OKChain through the Command-Line Interface (CLI).


身份注册及数字资产交易对发行
--------------------------



注册DEX运营方
~~~~~~~~~~~~

DEX运营方是OKChain中负责运营数字资产交易对的角色。通过在链上\ `注册DEX运营方 <>`__\ 后，拥有数字资产交易对的管理权利，每一个数字资产交易对都会属于一个DEX运营方。

DEX运营方的基础属性。官方网站，logo，交易入口，app下载链接，第三方社交账号等。

::

    此部分参考EOS的bp.json 设计 operation.json
    https://www.eoshuobipool.com/bp.json 
    https://www.eosx.io/
    https://www.eosx.io/account/eoshuobipool
    1.运行creat Operator [官方网站] 创建DEX运营方
    2.编写operation.json上传到“官方网站/operation.json”
    3.后期可以通过修改[官方网站] 属性，用户把[官方网站]更新为空可以视为网站更新维护/运营商跑路/交易所下线等场景

operation.json模板

.. code:: json

    {
      "dex_name": "eoshuobipool",
      "dex_owner_key": "okchain1nz77nuffa72redqv4n9hjqfw0vp54nyyjfuc30",
      "org": {
        "website": "http://www.eoshuobipool.com",
        "code_of_conduct":"",
        "email":"eoshuobipool@huobi.com",
        "branding":{
          "logo_256":"http://www.eoshuobipool.com/logo/EOS-256.png",
          "logo_1024":"http://www.eoshuobipool.com/logo/EOS-1024.png",
          "logo_svg":"http://www.eoshuobipool.com/logo/EOS-logo.svg"
        },
        "location": {
          "name": "Beijing",
          "country": "CN",
          "latitude": 40.060599,
          "longitude": 116.32371
        },
        "social": {
          "steemit": "eoshuobipool",
          "twitter": "EOS_huobipool",
          "youtube": "",
          "facebook": "",
          "github":"",
          "reddit": "",
          "keybase": "orcoder",
          "telegram": "https://t.me/eoshuobipool"
        }
      },
      "nodes": [
        {
          "location": {
            "name": "HuobiNode1",
            "country": "CN",
            "latitude": 40.060599,
            "longitude": 116.32371
          },
          "node_type": "query",
          "p2p_endpoint": "peer1.eoshuobipool.com:18181",
          "api_endpoint": "http://peer1.eoshuobipool.com:8181",
          "ssl_endpoint": "https://api.redpacketeos.com"
        },
        {
          "location": {
            "name": "HuobiNode2",
            "country": "CN",
            "latitude": 40.060599,
            "longitude": 116.32371
          },
          "node_type": "query",
          "p2p_endpoint": "peer2.eoshuobipool.com:18181",
          "api_endpoint": "http://peer2.eoshuobipool.com:8181",
          "ssl_endpoint": "https://api.redpacketeos.com"
        }
      ]
    }

OKChain的区块链浏览器就可以通过读取operation.json直接获取DEX运营方的相关数据。

发行自己的数字资产和交易对
~~~~~~~~~~~~~~~~~~~~~~~~

DEX运营商可以在任意时间发行自己的数字资产及交易对，出于安全的考虑，DEX运营方可以通过\ `代理功能 <>`__\ 指定代理账户发行自己的数字资产及交易对。

为自己的数字资产交易对添加撮合金
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

为了公平，开放的使用区块链的撮合资源，OpenDEX采用竞价排名的方式分配系统资源，DEX可以通过添加\ **`数字资产撮合金 <>`__**\ ，使自己交易对的撮合被优先处理。

流量入口及服务器
--------------------------

运行OKChain的全节点
~~~~~~~~~~~~~~~~~~~~~~~~

OKChain-OpenDEX采用链上订单簿管理和链上撮合的设计，因此DEX所需要的订单数据和行情数据需要从全节点数据中获取，查看\ `如何运行OKChain全节点 <>`__\ 。

启动数据插件
~~~~~~~~~~~~~~~~~~~~~~~~

依托于OKChain的\ `数据分层 <>`__\ 设计，我们将部分数据存到了链外，详情参见\ `keeper设计 <>`__\ 。OKChain-OpenDEX提供了两个插件方案，分别是\ `Backend模块插件 <>`__\ 和\ `Stream模块插件 <>`__\ 。

`Backend模块 <>`__\ 采用轻量级sqlite作为链外数据存储层，提供了基础的订单数据和行情数据的查询\ `接口 <>`__\ 。如果想要更好的服务，可以通过\ `Stream模块 <>`__\ 将链上数据导入到数据中间件中，配合专门的推送及行情计算服务进行输出。

扩展阅读：
`如何运用Stream模块构建高效的DEX行情和推送服务 <>`__\ ``此处跳转到项目博客``

对接流量入口
~~~~~~~~~~~~~~~~~~~~~~~~

虽然通过OKChain命令行可以可以使用DEX的所有操作（下单，撤单），但是DEX作为一个交易应用，功能更全更完善的可视化交易辅助工具会给交易者提供最直接的帮助，因此DEX运营方可以自行选择自己的流量入口，既可以查看\ `API接口设计 <>`__\ 定制自己的WEB端或者移动端，也可以选择由社区提供的\ `OpenDEX-UI <>`__\ ，快速启动一个交易所模板。
