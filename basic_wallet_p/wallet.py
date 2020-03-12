import requests
import json

r = requests.get('http://localhost:5000/chain')

data = r.json()
chain = data['chain']

id = input("Enter an id to track: ")

transactions = []
coins = 0

for block in chain:
    for t in block.get('transactions'):
        if t['recipient'] == id:
            coins += t['amount']
            transactions.append(t)
        elif t['sender'] == id:
            coins -= t['amount']
            transactions.append(t)

print(f'Coin total for {id}: {coins}\n')
print(f'Transactions for {id}:')
for t in transactions:
    sender = t['sender']
    recipient = t['recipient']
    amount = t['amount']
    print("------------------------------")
    print(f'Sender: {sender}')
    print(f'Recipient: {recipient}')
    print(f'Amount: {amount}')
    print("------------------------------")
