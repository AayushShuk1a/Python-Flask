class OutOfBoundException(ValueError):
    pass

class Book:
    def __init__(self,name,pages) -> None:
        self.name=name
        self.pages=pages
        self.pages_read=0

    def __str__(self) -> str:
        return f"{self.name} Has Total {self.pages} pages"
    
    def read(self,pages_read):
        count=self.pages_read+pages_read
        if count>self.pages:
            raise OutOfBoundException(
                f"Total Pages are {self.pages} pages, You cannot read {count} pages "
            )
        
        self.pages_read=count
        print(f"You have read {self.pages_read} pages, {self.pages-self.pages_read} pages left!")


try:
    book=Book("Harry Potter",600)
    book.read(300)
    book.read(350)
except OutOfBoundException as e:
    print(e)