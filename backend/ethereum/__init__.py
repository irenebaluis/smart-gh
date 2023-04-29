from web3 import Web3
import json

ganache_url = "http://127.0.0.1:8545"

# Create the node connection
WEB3 = Web3(Web3.HTTPProvider(ganache_url))

# Verify if the connection is successful
if WEB3.is_connected():
    print("-" * 50)
    print("Connection Successful")
    print("-" * 50)
else:
    print("Connection Failed")



# Initialize contract ABI and address
abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"_userID","type":"uint256"}],"name":"approveUser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_userID","type":"uint256"}],"name":"deleteUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"getUserLog","type":"event"},{"inputs":[{"internalType":"address","name":"_userAddress","type":"address"},{"internalType":"string","name":"_userRole","type":"string"},{"internalType":"string","name":"_email","type":"string"},{"internalType":"bool","name":"_isApproved","type":"bool"}],"name":"register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllUsers","outputs":[{"components":[{"internalType":"uint256","name":"userID","type":"uint256"},{"internalType":"address","name":"userAddress","type":"address"},{"internalType":"string","name":"userRole","type":"string"},{"internalType":"string","name":"email","type":"string"},{"internalType":"bool","name":"isApproved","type":"bool"},{"internalType":"bool","name":"set","type":"bool"}],"internalType":"struct UserRegistration.User[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_userID","type":"uint256"}],"name":"getUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_userID","type":"uint256"}],"name":"isAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userAddress","outputs":[{"internalType":"uint256","name":"userID","type":"uint256"},{"internalType":"address","name":"userAddress","type":"address"},{"internalType":"string","name":"userRole","type":"string"},{"internalType":"string","name":"email","type":"string"},{"internalType":"bool","name":"isApproved","type":"bool"},{"internalType":"bool","name":"set","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"users","outputs":[{"internalType":"uint256","name":"userID","type":"uint256"},{"internalType":"address","name":"userAddress","type":"address"},{"internalType":"string","name":"userRole","type":"string"},{"internalType":"string","name":"email","type":"string"},{"internalType":"bool","name":"isApproved","type":"bool"},{"internalType":"bool","name":"set","type":"bool"}],"stateMutability":"view","type":"function"}]')
contract_address = '0xF2c94BAa1c6e739B9635Fc31211F4AAcb83c7ADb'

# Create smart contract instance
CONTRACT = WEB3.eth.contract(address=contract_address,abi=abi)

# initialize the chain id, we need it to build the transaction for replay protection
CHAIN_ID = WEB3.eth.chain_id

