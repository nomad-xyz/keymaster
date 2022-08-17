from web3 import Web3

endpoint = "https://arb-rinkeby.g.alchemy.com/v2/1od885gmhmXies1Gluk-Yb9027xnYYIv"
sender_key = "0xb09c0011111111111111111111111111111111111111111111111111cece1000"
recipient_address = "0x61f5757848bBB72bAD2963dBae99F948E1085251"

w3 = Web3(Web3.HTTPProvider(endpoint))
recipient_address = Web3.toChecksumAddress(recipient_address)
chain_id = w3.eth.chain_id

# sign transaction 
tx_params = dict(
    nonce=12,
    gasPrice= 500 * 10 ** 9,
    gas=10000000,
    to=recipient_address,
    value=int(5e+17),
    data=b'',
    chainId=chain_id,
)

signed_txn = w3.eth.account.sign_transaction(tx_params, sender_key)
#hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)  

print(signed_txn)
