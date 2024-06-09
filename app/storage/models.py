import enum

from sqlalchemy import Integer, String, BigInteger, ForeignKey, Enum
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy.types import Date


class Base(DeclarativeBase):
    pass


class SocialNetworksEnum(enum.Enum):
    VK = 'vk'
    IG = 'ig'


class Post(Base):
    __tablename__ = 'post'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
    social_network: Mapped[SocialNetworksEnum] = mapped_column(Enum(SocialNetworksEnum), nullable=False)
    link: Mapped[String] = mapped_column(String(200), unique=True, nullable=False)
    date_published: Mapped[Date] = mapped_column(Date, nullable=False)
    views: Mapped[Integer] = mapped_column(Integer, nullable=True)
    likes: Mapped[Integer] = mapped_column(Integer, nullable=True)
    author: Mapped[String] = mapped_column(String(200), nullable=False)
    hashtag_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('hashtag.id'))

    hashtag = relationship('Hashtag', cascade='all, delete', back_populates='post')

    def __repr__(self):
        return f'Post id={self.id}'


class Hashtag(Base):
    __tablename__ = 'hashtag'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
    name: Mapped[String] = mapped_column(String(200), unique=True, nullable=False)
    post = relationship('Post', cascade='all, delete', back_populates='hashtag')

    def __repr__(self):
        return f'Hashtag id={self.id}'
