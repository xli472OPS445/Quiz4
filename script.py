#!/usr/bin/env python3
# Author: xli472


class CashRegister:
 
    def __init__(self, name):
        self.name = name 
        self.transactions = []

    def __str__(self):
        return f'{self.name}'s cash register with {self.balance:2f} transactions'
    
    def __repr__(self):
        return f'Today's balance: $ {self.balance:2f}'
 
    def transaction(self, amt):
        self.transactions.append(amt)
        self.balance = sum(self.transactions)
        return self.transactions 




