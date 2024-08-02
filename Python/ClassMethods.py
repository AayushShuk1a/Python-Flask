class Books:
    Types=("HardCover", "PaperBack")

    def __init__(self,name,type,weigth):
        self.name=name
        self.type=type
        self.weigth=weigth

    def __str__(self) -> str:
        return f"Name {self.name}, Type {self.type}, Weigth {self.weigth}g"
    
    @classmethod
    def hardCover(cls,name,weight):
        return cls(name,cls.Types[0],weight+100)
    
    @classmethod
    def paperBack(cls,name,weight):
        return cls(name,cls.Types[1],weight)
    

book1=Books("Wolverine","Comic Book", 200)  #init function
print(book1)

book2=Books.hardCover("Harry Potter",1500) #hardCover class Method function
print(book2)

book3=Books.paperBack("One Piece",200) #paperBack class Method