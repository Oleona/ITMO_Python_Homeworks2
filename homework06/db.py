from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework06.scraputils import get_news

Base = declarative_base()
engine = create_engine("sqlite:///news.db")
session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(Integer)
    points = Column(Integer)
    label = Column(String)


Base.metadata.create_all(bind=engine)

s = session()
new = get_news("https://news.ycombinator.com/newest", n_pages=6)
for item in new:
    news = News(title=item['title'],
                author=item['author'],
                url=item['url'],
                comments=item['comments'],
                points=item['points'])
    s.add(news)
s.commit()
