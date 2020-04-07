DEX Operations Guide (CLI)
==============================

This document contains all the necessary information for DEX operations to interact with the OKChain through the Command-Line Interface (CLI).


Identity registration & digital asset transaction pair issuance
------------------------------------------------------------------



Registered DEX Operator
~~~~~~~~~~~~~~~~~~~~~~~~~~


The DEX operator is the role in OKChain responsible for operating digital asset trading pairs. By `registering the DEX operator <>`__  on the chain, you have the right to manage digital asset trading pairs, and each digital asset trading pair will belong to a DEX operator.

The basic attributes of the DEX operator. Official website, logo, transaction entrance, app download link, third-party social account, etc.


operation.json Template

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

OKChain's blockchain browser can directly obtain the relevant data of the DEX operator by reading operation.json.

Issue your own digital assets and trading pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~

DEX operators can issue their own digital assets and trading pairs at any time. For security reasons, DEX operators can issue their own digital assets and trading pairs through the designated agent account of \ `Agency Function <>`__ \.

Add alloys to your own digital asset trading pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to be fair and open to use the matching resources of the blockchain, OpenDEX uses bid ranking to allocate system resources. DEX can make matching of its own trading pairs by adding \ ** `digital asset matching alloy <>`__ ** \ Priority.

Traffic entrance and server
--------------------------

Full node running OKChain
~~~~~~~~~~~~~~~~~~~~~~~~~~

OKChain-OpenDEX adopts the design of on-chain order book management and on-chain matching, so the order data and market data needed by DEX need to be obtained from the full node data, see \ `How to run OKChain full node <>`__ \.

Start the data plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~

Relying on OKChain's \ `data layering <>`__ \ design, we saved part of the data outside the chain. For details, see \ `keeper design <>`__ \. OKChain-OpenDEX provides two plug-in solutions, namely \ `Backend module plug-in <>`__ \ and \ `Stream module plug-in <>`__ \.

`Backend module <>`__ \ uses lightweight sqlite as the off-chain data storage layer, providing basic order data and market data query \ `Interface <>`__ \. If you want a better service, you can import the data on the chain into the data middleware through the \ `Stream module <>`__ \, and output it with a special push and market calculation service.

Further reading:
`How to use the Stream module to build an efficient DEX market and push service <>`__ \ `` Jump here to the project blog``

Docking traffic entrance
~~~~~~~~~~~~~~~~~~~~~~~~~~

Although all operations of DEX (order placing, order cancellation) can be used through the OKChain command line, DEX is a trading application with more complete and complete visual trading assistance tools that will provide the most direct help to traders, so DEX operations The party can choose its own traffic entrance, either view \ `API interface design <>`__ \ to customize its own WEB or mobile terminal, or choose \ `OpenDEX-UI <>`__ \ provided by the community, fast Start an exchange template.


