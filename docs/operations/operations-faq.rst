DEX Operations FAQ
====================



What is  DEX Operations? Why do we need DEX Operations?
------------------------------------------------------------------------

The DEX Operator is an entity that operates a decentralized exchange. His core assets are the digital asset trading pairs he operates, and his value is reflected through the operation of digital asset trading pairs. Generally speaking, the DEX operator only needs to provide a `flow entrance <>`__  and basic liquidity supply.

Why do we need DEX Operators?
-----------------------------------------------------------

Whether it is a centralized exchange or a decentralized exchange, it is to solve the replacement needs of digital assets.

In the development history of human beings, we can intuitively recognize that at the same technical level, centralization is the most effective way to improve efficiency, that is, let professional people do professional things. This is why centralized exchanges that focus on efficiency will develop more quickly than decentralized exchanges.

But in fact, not all things need to be solved in the most efficient way. After the centralized exchange meets the need for partial efficiency in the replacement demand, those neglected scenarios, such as those that focus more on security or fairness, are also urgently needed. solve. In the blockchain world, it is reflected in the credit risk of fund entrustment, so decentralized exchanges are a trading system for this point, so centralized exchanges and decentralized exchanges are not an alternative relationship, and It is a complementary brotherhood.

Furthermore, an exchange actually assumes the role of ** Zengxin ** \ in the ecosystem. The same is true for decentralized exchanges, so the operator of a decentralized exchange is the main body of this role. In the traditional concept, the main body of this \ ** Zengxin ** \ role is usually defined as the technology, that is, the public chain itself, but based on the market ’s feedback on such projects in recent years, we believe that the user does not approve This program.

Analyzing the reasons, we believe that there is a lack of operating entities. Like the e-commerce model we are exposed to, Taobao is a platform, and it is Taobao sellers who really provide services to users. The platform of Taobao plays a credit-enhancing service for this seller, but it does not mean that the merchant can not do any commercial operations. In order to highlight the characteristics of decentralization, the traditional decentralized exchange model puts too much emphasis on the platform and can ignore the business itself as the main operating entity.

Therefore, the DEX operator in OKChain is proposed to solve this problem.

Why can't DEX Operators be chain-operators?
---------------------------------------------------


If there is only one operator on a chain, the ecology of this chain is also closed. As early as 2013, projects have conducted experiments of such models, but their development has been restricted due to the limitation of the closed ecology. Learn more  **`Chain matching fee design <>`__**. Therefore, if you want an open DEX ecosystem, the public chain operator cannot undertake all the work of DEX operations.

Therefore, a new design challenge is also raised, namely how to make all DEX operators use the blockchain resources fairly and openly.

For example, the management of trading pairs such as the issuance of  `digital asset trading pairs <>`__  should be the same as \ `Issuing digital assets <>` __ \, because it is the core of the DEX operator. Assets are also the most basic needs. At the same time, for the use of the matching engine, if the system carries variable value digital asset trading pairs, when the system resources are insufficient, OpenDEX also introduced \ ** `" Digital Asset Matching Alloy "<>` __ ** \ The concept of allocating system resources through auction ranking is adopted through a mechanism similar to lock-up.

DEX Operators costs
--------------------------

The value of DEX operators is reflected through the operation activities of digital asset trading pairs. In the blockchain system, application developers do not need to bear the server cost, only the development cost and the deployment cost of the DAPP application, and the design fee is essentially the revenue that the block node sells its computing and storage resources. Therefore, all the handling fees are distributed to the block nodes as revenue. Therefore, in the traditional DEX scheme, it is mandatory to allocate the handling fee of the matching part to the fast node, also because the block node is the DEX operator. In OpenDEX, the DEX operator has been distinguished from the public chain operator, so the matching commission fee caused by the matching is returned to the DEX operator itself, in order to solve the traditional DEX scheme because of the high cost of market making. The resulting liquidity problem. Read  `Handling fee design <>`__ to learn more.