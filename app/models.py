from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base

address_users = Table(
    'address_users', Base.metadata,
    Column('address_id', Integer, ForeignKey('addresses.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    addresses = relationship("Address", secondary=address_users, back_populates="users")


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    place = Column(String)

    users = relationship("User", secondary=address_users, back_populates="addresses")
