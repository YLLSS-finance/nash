
from sortedcontainers import SortedSet
from order import order
import time as t

class accountContract:
    def __init__(self):
        self._master = None
        self.contractID = 'contract'
        self._id = 0
        # exposing some functions and objects from the account class
        #self.mpid = self._master.mpid
        self.mpid = 'bob'
        
        # adds an order object to account's order dictionary and respective exchange orderbook
        #self.addOrder = self._master.addOrder
        self.globalAddOrder = print
        
        # Change base token amount for transactions
        self.chg = print
        
        self.position = [0, 0]
        self.reducible = [0, 0]
        
        self.red = (SortedSet(), SortedSet())
        self.inc = (SortedSet(), SortedSet())
    
    def getNewOrderQty(self, side, qty):
        reduceQty = min(qty, self.reducible[1 - side])
        increaseQty = qty - reduceQty
        return reduceQty, increaseQty

    def addOrder(self, price, side, qty):
        red, inc = self.getNewOrderQty(side, qty)
        # TODO: CHECK COST
        
        self.reducible[1 - side] -= red
        ordr = order(
            _master = self,
            orderID = self._id, 
            contractID = self.contractID,
            mpid = self.mpid, 
            timestamp = round(1000 * t.time()), 
            price = price, 
            side = side, 
            inc = inc,
            red = red
        )
        self._id += 1
        redOrders, incOrders = self.red[side], self.inc[side]
        
        while True:
            if len(redOrders) == 0:
                break
            result = redOrders[-1].convertOrdr(ordr)
            if result is False:
                break
            
        self.globalAddOrder(ordr)
        self.chg(ordr.incCost * ordr.inc * -1)
        ordr.updateOrder()

test = accountContract()
val = [0, 25]
test.position = val
test.reducible = val
test.addOrder(8, 0, 10)
test.addOrder(7, 0, 10)
print('red', test.reducible)
print(test.red[0])
test.addOrder(9, 0, 10)