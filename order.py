 
class order:
    def __init__(self, _master, orderID, mpid, timestamp, contractID, price, side, red, inc):
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