Delegators Guide (CLI)
==============================

This document contains all the necessary information for delegators to interact with the OKChain through the Command-Line Interface (CLI).


Voting Mechanics
---------------------

In OKChain, any user who has staked OKT tokens can vote. Each user is allowed to vote for up to 30 block producer candidates using the full weight of their stake. For example, if a user has 1000 OKT staked, she can cast 1000 votes each for up to 30 Validators. The top 21 block producer candidates by total number of votes received form the core set of validators. Additional Validators, ranked by total votes, are also compensated by the network to serve as Validator Candidates.

OKChain is a liquid, delegative democracy. Users have the option of voting directly for Validators, but they can also delegate their voting power to another account to vote on their behalf. The delegate account, called a proxy, has no control over the original user’s account — the user can proxy her vote trustlessly without handing over any keys. The proxy simply has the power to direct that user’s voting power towards certain Validators, but the user can revoke her voting power from the proxy at any point.

Installing okchaincli
--------------------------

okchaincli：This is the command-line interface to interact with a `okchaind` full-node.

| Currently, ``OKChain`` is not open source. You can download the
executable programs ``okchaind`` and ``okchaincli`` through the
`official website <https://github.com/ok-chain/binaries>`__.
| After downloading successfully, you can use the related functions of
``OKChain``.

    Note: The current version of ``OKChain`` used by the testnet is
    ``v0.1.0``.

okchaincli is a command-line client of OKChain that offers rich
functions to interact with the backend application of OKChain. It mainly
includes two types of functions: tx function and query function. For
further information, please refer to ``okchaincli -h`` as follows:

.. code:: sh

    $ okchaincli -h
    OKChain Client

    Usage:
      okchaincli [command]

    Available Commands:
      status      Query remote node for status
      config      Create or query an OKChain CLI configuration file
      query       Querying subcommands
      tx          Transactions subcommands
      backend     backend subcommands


      keys        Add or view local private keys

      version     Print the app version
      help        Help about any command

    Flags:
          --chain-id string   Chain ID of tendermint node
      -e, --encoding string   Binary encoding (hex|b64|btc) (default "hex")
      -h, --help              help for okchaincli
          --home string       directory for config and data (default "/Users/hanxueyang/.okchaincli")
      -o, --output string     Output format (text|json) (default "text")
          --passwd string     Pass word of sender (default "12345678")
          --trace             print out full stack trace on errors

    Use "okchaincli [command] --help" for more information about a command.

Meanwhile, users can also manage local private keys through the
sub-command ``okchaincli keys``.

OKChain Accounts
-------------------
At the core of every OKChian account, there is a seed, which takes the form of a 12-words mnemonic. From this mnemonic, it is possible to create any number of Cosmos accounts, i.e. pairs of private key/public key. This is called an HD wallet (see `BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`__ for more information on the HD wallet specification).

The funds stored in an account are controlled by the private key. This private key is generated using a one-way function from the mnemonic. If you lose the private key, you can retrieve it using the mnemonic. However, if you lose the mnemonic, you will lose access to all the derived private keys. Likewise, if someone gains access to your mnemonic, they gain access to all the associated accounts.

.. note::
     Do not lose or share your 12 words with anyone. To prevent theft or loss of funds, it is best to ensure that you keep multiple copies of your mnemonic, and store it in a safe, secure place and that only you know how to access. If someone is able to gain access to your mnemonic, they will be able to gain access to your private keys and control the accounts associated with them.

The address is a public string with a human-readable prefix (e.g. ``okchain1v853tq96n9ghvyxlvqyxyj97589clccr33yr7a``) that identifies your account. When someone wants to send you funds, they send it to your address. It is computationally infeasible to find the private key associated with a given address.

Creating an Account
>>>>>>>>>

To create an account, you just need to have ``okchaincli`` installed. Before creating it, you need to know where you intend to store and interact with your private keys. The best options are to store them in an offline dedicated computer or a ledger device. Storing them on your regular online computer involves more risk, since anyone who infiltrates your computer through the internet could exfiltrate your private keys and steal your funds.

Using a Computer
::::::::::::::::

.. note::
   It is more secure to perform this action on an offline computer :::

To generate an account, just use the following command:

.. code:: bash
   okchaincli keys add <name> [flags]

The command will generate a 12-words mnemonic and save the private and public keys for account 0 at the same time. Each time you want to send a transaction, you will need to unlock your system's credentials store. If you lose access to your credentials storage, you can always recover the private key with the mnemonic.

.. note::
   After you have secured your mnemonic (triple check!), you can delete bash history to ensure no one can retrieve it:

.. code:: bash
    history -c
    rm ~/.bash_history

