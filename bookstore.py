
from pydantic import BaseModel,Field
from collections import defaultdict
from uuid import UUID,uuid4


from enum import Enum

#search Criteria

class SearchCriteria(Enum):
    Multi_criteria="Multi_criteria"
    Simple_Search="Simple_search"



#Book model
class Book(BaseModel):
    id:UUID=Field(default_factory=uuid4)
    name:str
    author:str
    description:str
    year_release:int = Field(title="Year released",ge=1900,le=2100)


#Book methods 
class Bookstore:
    def __init__(self):
        self.books={}
    def create_book(self, title: str, author: str, description: str, year_release: int) -> Book:
            # Validate input
            if not title or not author:
                raise ValueError("Title and author are required")
            
            # Create Book object
            book = Book(
                name=title,
                author=author,
                description=description,
                year_release=year_release
            )
            
            # Add to bookstore
            self.add_book(book)
            return book
    def add_book(self,book:Book)->Book:
        ''' Takes a Book object from Book model
        args:Book
        returns a Book object
        '''
        #add the book to the list
        self.books[book.id] = book
        return book

    def remove_book(self,book_id:UUID)->Book | None:
        if book_id in self.books:
            del self.books[book_id]

    def get_book(self, book_id: UUID) -> Book | None:
        return self.books.get(book_id)
    


    #will switch to convex search soon
    def search_book(self,search_method=SearchCriteria.Multi_criteria,Pagination=10)->dict:
        '''
        multi-search name and author
        '''

        #something happen
        search_result={}

        return search_result
        
        
    def get_all(self)->list:
        return self.books
        

if __name__ == "__main__":
    bookstore = Bookstore()
    #create a book
    bookstore.create_book()
    print(bookstore.get_all())
  
    





