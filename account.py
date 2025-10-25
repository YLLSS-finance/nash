class account:
    def __init__(self, _master, acctData):
        # the master is the main exchange class
        self._master = _master
        
        self.mpid = acctData['mpid']
        self.tokens = acctData['tokens']
        self.orders = {}
        #test
        for contractName, contractData in acctData['contracts']:
            