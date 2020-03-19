Delegators FAQ
====================


What is a delegator?
---------------------------------------

People that cannot or do not want to operate validator nodes can still participate in the staking process as delegators. Indeed, validators are not chosen based on their self-delegated stake but based on their total stake, which is the sum of their self-delegated stake and of the stake that is delegated to them. This is an important property, as it makes delegators a safeguard against validators that exhibit bad behavior. If a validator misbehaves, their delegators will move their Atoms away from them, thereby reducing their stake. Eventually, if a validator's stake falls under the top 100 addresses with highest stake, they will exit the validator set.

Delegators share the revenue of their validators, but they also share the risks. In terms of revenue, validators and delegators differ in that validators can apply a commission on the revenue that goes to their delegator before it is distributed. This commission is known to delegators beforehand and can only change according to predefined constraints (see section below). In terms of risk, delegators' Atoms can be slashed if their validator misbehaves. For more, see Risks section.

To become delegators, Atom holders need to send a "Delegate transaction" where they specify how many Atoms they want to bond and to which validator. A list of validator candidates will be displayed in Cosmos Hub explorers. Later, if a delegator wants to unbond part or all of their stake, they needs to send an "Unbond transaction". From there, the delegator will have to wait 3 weeks to retrieve their Atoms. Delegators can also send a "Rebond Transaction" to switch from one validator to another, without having to go through the 3 weeks waiting period.

For a practical guide on how to become a delegator, click here.

Choosing a validator
--------------------------

In order to choose their validators, delegators have access to a range of information directly in Lunie or other Cosmos block explorers.

- **Validator's moniker**: Name of the validator candidate.
- **Validator's description**: Description provided by the validator operator.
- **Validator's website**: Link to the validator's website.


Directives of delegators
---------------------------------------

Being a delegator is not a passive task. Here are the main directives of a delegator:

- **Perform careful due diligence on validators before delegating.** If a validator misbehaves, part of their total stake, which includes the stake of their delegators, can be slashed. Delegators should therefore carefully select validators they think will behave correctly.
- **Actively monitor their validator after having delegated.** Delegators should ensure that the validators they delegate to behave correctly, meaning that they have good uptime, do not double sign or get compromised, and participate in governance. They should also monitor the commission rate that is applied. If a delegator is not satisfied with its validator, they can unbond or switch to another validator (Note: Delegators do not have to wait for the unbonding period to switch validators. Rebonding takes effect immediately).
- **Participate in governance.** Delegators can and are expected to actively participate in governance. A delegator's voting power is proportional to the size of their bonded stake. If a delegator does not vote, they will inherit the vote of their validator(s). If they do vote, they override the vote of their validator(s). Delegators therefore act as a counterbalance to their validators.
