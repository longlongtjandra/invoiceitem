class InvoiceItem:
    def __init__(self,id,desc,qty,unitPrice):
        self.__id = str(id)
        self.__desc = str(desc)
        self.__qty = int(qty)
        self.__unitprice = float(unitPrice)

    def getID(self):
        return str(self.__id)

    def getDesc(self):
        return str(self.__desc)

    def getQty(self):
        return int(self.__qty)

    def setQty(self,qty):
        self.__qty = qty

    def getunitprice(self):
        return (self.__unitprice) vc

    def setunitprice(self,unitPrice):
        self.__unitprice = unitPrice

    def getTotal(self):
        return (self.__qty)*(self.__unitprice)

    def toString(self):
        print("InvoiceItem[id={},desc={},qty={},unitprice={}]".format(self.__id,self.__desc,self.__qty,self.__unitprice))


