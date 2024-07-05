from datetime import datetime

from sqlalchemy import Integer, String, BigInteger, ForeignKey, Enum, UniqueConstraint, func, DateTime
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy.types import Date

from app.schemas.common import SocialNetworksEnum


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = 'post'
    __table_args__ = (
        UniqueConstraint('author_id', 'resource_id', 'type', name='uq_publication'),
    )

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
    social_network: Mapped[SocialNetworksEnum] = mapped_column(Enum(SocialNetworksEnum), nullable=False)
    type: Mapped[String] = mapped_column(String(200), nullable=True)
    author_id: Mapped[Integer] = mapped_column(Integer, nullable=True)
    resource_id: Mapped[Integer] = mapped_column(Integer, nullable=True)
    date_published: Mapped[Date] = mapped_column(Date, nullable=False)
    views: Mapped[Integer] = mapped_column(Integer, nullable=True)
    likes: Mapped[Integer] = mapped_column(Integer, nullable=True)
    updated_at: Mapped[Date] = mapped_column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
    hashtag_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('hashtag.id'))

    hashtag = relationship('Hashtag', cascade='all, delete', back_populates='posts')

    def __repr__(self):
        return f'Post id={self.id}'


class Hashtag(Base):
    __tablename__ = 'hashtag'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, autoincrement=True, index=True)
    name: Mapped[String] = mapped_column(String(200), unique=True, nullable=False)
    campaign_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('campaign.id'))

    posts = relationship('Post', cascade='all, delete', back_populates='hashtag')
    campaign = relationship('Campaign', cascade='all, delete', back_populates='hashtags')

    def __repr__(self):
        return f'Hashtag {self.name}'


class Campaign(Base):
    __tablename__ = 'campaign'

    id: Mapped[BigInteger] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True, index=True)
    name: Mapped[String] = mapped_column(String(200), unique=True, nullable=False)

    hashtags = relationship('Hashtag', cascade='all, delete', back_populates='campaign')

    def __repr__(self):
        return f'Campaign {self.name}'
