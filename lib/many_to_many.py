class Author:
    list_of_authors = []

    def __init__(self, name):
        self.name = name
        self.list_of_authors.append(self)
    
    def contracts(self):
        related_contracts =[]
        for contract in Contract.list_of_contracts:
            if contract.author == self:
                related_contracts.append(contract)
        return related_contracts

    def books(self):
        related_books = []
        for contract in Contract.list_of_contracts:
            if contract.author == self:
                related_books.append(contract.book)
        return related_books

    def sign_contract(self, book, date, royalties):
         new_obj = Contract(self, book, date, royalties)
         return new_obj



    def total_royalties(self):
        related_royalties =[]
        for contract in Contract.list_of_contracts:
            if contract.author == self:
                related_royalties.append(contract.royalties)
        return sum(related_royalties)
    


class Book:

    list_of_books = []

    def __init__(self, title):
        self.title = title 
        self.list_of_books.append(self)

    def contracts(self):
        related_contracts =[]
        for contract in Contract.list_of_contracts:
            if contract.book == self:
                related_contracts.append(contract)
        return related_contracts
    
    def authors(self):
        related_authors = []
        for contract in Contract.list_of_contracts:
            if contract.book == self:
                related_authors.append(contract.author)
        return related_authors


class Contract:

    list_of_contracts = []

    def __init__(self, author, book, date, royalties):
        if  author in Author.list_of_authors:
            self.author = author
        else:
            raise Exception
        if book in Book.list_of_books:
             self.book = book
        else:
            raise Exception
        if isinstance(date, str):
            self.date = date 
        else:
            raise Exception
        if isinstance(royalties, int):
            self.royalties = royalties 
        else:
            raise Exception
        Contract.list_of_contracts.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(Contract.list_of_contracts, key=lambda obj: obj.date)
       
