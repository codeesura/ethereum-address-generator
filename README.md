# Ethereum Address Generator

This is a Python script that generates Ethereum addresses and private keys. It uses the web3 library to create accounts and applies some filtering conditions to save specific addresses.

## Prerequisites

To successfully run this code, ensure the following Python libraries are installed:

- `web3`: A Python library for interacting with Ethereum.
- `json`: A standard Python library for handling JSON data.

If you haven't installed these libraries, you can install them using pip:

```shell
pip install web3
```

## Usage

To use the script, execute it with Python 3. The script will continually generate Ethereum accounts until manually stopped. It evaluates each generated account based on the following conditions:

- If the Ethereum address begins with "0xSPECIFIC1".
- If the Ethereum address begins with "0xSPECIFIC2".
If an Ethereum account fulfills these conditions, the account's address and private key are written to a JSON file, 'wallet.json'. The JSON file has the following structure:

```json
{
    "wallets": [
        {
            "address": "account_address",
            "private_key": "account_private_key"
        },
        ...
    ]
}
```
The script can be stopped by interrupting it (for instance, pressing CTRL+C in the console).

## Security Warning
**NEVER SHARE YOUR PRIVATE KEYS!** Private keys are extremely sensitive data that grant full control over the corresponding Ethereum account to anyone possessing them. Always keep them safe and secure.

## Disclaimer
This script is intended for educational use only. It should not be used for illicit activities. codeesura is not responsible for any misuse of this script.
