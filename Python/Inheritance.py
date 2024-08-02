class Device:
    def __init__(self,name,connectedBy):
        self.name=name
        self.connectedBy=connectedBy
        self.connected=True

    def __str__(self):
        return f"Device {self.name}, Connected By {self.connectedBy}"
    
    def disconnect(self):
        self.connected=False
        print("Disconnected")


class Printer(Device):
    def __init__(self,name,connectedBy,capacity):
        super().__init__(name,connectedBy)
        self.capacity=capacity
        self.remainingPages=capacity
    def __str__(self):
        return f"{super().__str__()} , Capacity left is {self.remainingPages}"
    
    def print(self,pages):
        if self.connected==False:
            print("Please connect the device")
            return
        
        print(f"Printing {pages} pages")
        self.remainingPages-=pages


printer=Printer("Printer","USB", 500)

printer.print(20)
print(printer)
printer.disconnect()

printer.print(30)
        