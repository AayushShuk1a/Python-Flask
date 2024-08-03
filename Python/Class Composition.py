class Bookshelf:
    def __init__(self,*books):
        self.books=books

    def __str__(self) -> str:
        return f"Books : {tuple(str(book) for book in self.books)}"
    

class Books:
    def __init__(self,name,page) -> None:
        self.name=name
        self.pages=page

    def __str__(self) -> str:
        return f"Name : {self.name} , Pages :{self.pages}"
    


book1=Books("Shoe Dog",250)
book2=Books("The Alchemist",160)

shelf=Bookshelf(book1,book2)
        
print(shelf)