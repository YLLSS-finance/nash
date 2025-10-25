
from sortedcontainers import SortedSet
from order import order
import time as t

class accountContract:
    def __init__(self):
        self._master = None
        
        # exposing some functions and objects from the account class
        self.mpid = self._master.mpid
        
        # adds an order object to account's order dictionary and respective exchange orderbook
        self.addOrder = self._master.addOrder
        
        # Change base token amount for transactions
        self.chg = self._master.chg
        
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
        
        ordr = order(
            _master = self,
            orderID = id, 
            mpid = self.mpid, 
            timestamp = round(1000 * t.time()), 
            price = price, 
            side = side, 
            inc = inc,
            red = red
        )
        redOrders, incOrders = self.red[side], self.inc[side]
        
        while redOrders[-1] > ordr:
            
        

        