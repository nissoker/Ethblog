import json
from web3 import Web3


web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

web3.eth.defaultAccount = web3.eth.accounts[0]
abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"postId","type":"uint256"},{"indexed":false,"internalType":"string","name":"title","type":"string"}],"name":"NewPost","type":"event"},{"constant":false,"inputs":[{"internalType":"string","name":"_username","type":"string"},{"internalType":"string","name":"_date","type":"string"},{"internalType":"string","name":"_title","type":"string"},{"internalType":"string","name":"_content","type":"string"}],"name":"createPost","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getNumberOfPosts","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"_username","type":"string"}],"name":"getOwnerPostCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_postId","type":"uint256"}],"name":"getPost","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"_username","type":"string"},{"internalType":"uint256","name":"_pos","type":"uint256"}],"name":"getUsernamesPosts","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"ownerPostCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"postToOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"posts","outputs":[{"internalType":"string","name":"username","type":"string"},{"internalType":"string","name":"date","type":"string"},{"internalType":"string","name":"title","type":"string"},{"internalType":"string","name":"content","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_postId","type":"uint256"},{"internalType":"string","name":"_title","type":"string"},{"internalType":"string","name":"_content","type":"string"}],"name":"setPost","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"usernamesPosts","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
address = web3.toChecksumAddress("0x8f40D874eb3023a8829e10775B5257a76832cb13")

contract = web3.eth.contract(address= address, abi = abi)
#tx_hash = contract.functions.createPost("aniskerkouche",63578682,"title","this is my first blog").transact()
#web3.eth.waitForTransactionReceipt(tx_hash)
try:
	print(contract.functions.postToOwner(0).call())
except ValueError as err:
	print('coucour')