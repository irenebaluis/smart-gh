from .. import *


def build_transaction(caller):
    nonce = WEB3.eth.get_transaction_count(caller)
    caller = WEB3.to_checksum_address(caller)
    return {
        "gasPrice": WEB3.eth.gas_price,
        "chainId": CHAIN_ID,
        "from": caller,
        "nonce": nonce
    }


def sign_contract(call_function, private_key):
    # Sign transaction
    signed_tx = WEB3.eth.account.sign_transaction(call_function, private_key=private_key)

    # Send transaction
    send_tx = WEB3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Wait for transaction receipt
    WEB3.eth.wait_for_transaction_receipt(send_tx)
