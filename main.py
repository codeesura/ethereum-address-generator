from web3 import Web3
import json

w3 = Web3()

while True:
    account = w3.eth.account.create()
    address = account.address
    private_key = account.privateKey.hex()

    if address.startswith("0xSPECIFIC1") or address.startswith("0xSPECIFIC2"):
        with open('wallet.json', 'r') as f:
            wallet_data = json.load(f)
        wallet_data['wallets'].append({'address': address, 'private_key': private_key})
        with open('wallet.json', 'w') as f:
            json.dump(wallet_data, f,indent=4)
        
