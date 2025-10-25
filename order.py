 
class order:
    def __init__(self, _master, orderID, mpid, timestamp, contractID, price, side, red, inc):
        self._master = _master
        
        self.orderID = orderID
        self.mpid = mpid
        self.timestamp = timestamp
        self.contractID = contractID
        self.price = price
        self.side = side
        self.red = red
        self.inc = inc
    
        self.incCost = price if self.side == 0 else 100 - self.price
        self.comparisonKey = (-self.price if self.side == 0 else self.price, self.timestamp, self.orderID)
        
    
    def __lt__(self, other):
        return self.comparisonKey < other.comparisonKey
    
    def updateOrder(self):
        red = self._master.red[self.side]
        inc = self._master.inc[self.side]
        if self.red != 0:
            red.add(self)
        if self.red == 0:
            red.discard(self)
        if self.inc != 0:
            inc.add(self)
        if self.inc == 0:
            inc.discard(self)
    
    def move(self, qty):
        '''Transfers reduce quantity to increase quantity for a positive value and vice versa.'''
        self.inc += qty
        self.red -= qty
        self.updateOrder()
    
    
    def convertOrdr(self, incOrdr):
        '''Shifts reduce quantity of incoming order to increase quantity. Will cause margin allocation.'''
        if incOrdr.inc == 0:
            return False
        
        # Check if the reducing order already takes priority
        if incOrdr > self:
            print('red has prio')
            return False
                
        chgQty = min(incOrdr.inc, self.red)
        
        if chgQty == 0:
            return False
        
        self.move(chgQty)
        incOrdr.move(-chgQty)
        
        print('PAYMENT')
        self._master.chg(-self.incCost * chgQty)
        self.updateOrder()

        
        