from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(Date)


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert data
book1 = Book(title='The great gatsby', author='F.Scott Fitzgad', publication_date='2023-03-03')
book2 = Book(title='The great gatsby version two', author='F.Scott Fitzgad', publication_date='2024-04-09')
session.add(book1)
session.add(book2)
session.commit()

books = session.query(Book).all()
for book in books:
    print(f'{book.id}: {book.title} by {book.author}, published on {book.publication_date}')


def search_by_author(author_name):
    return session.query(Book).filter(Book.author == author_name).all()


author_books = search_by_author('Author A')
for book in author_books:
    print(f'{book.id}: {book.title} by {book.author}, published on {book.publication_date}')

session.close()
