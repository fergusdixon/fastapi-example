from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import RelationshipProperty, relationship

from app.db.base_class import Base

address_users = Table(
    "address_users",
    Base.metadata,  # type: ignore
    Column("address_id", Integer, ForeignKey("address.id")),
    Column("user_id", Integer, ForeignKey("user.id")),
)


class Address(Base):

    id = Column(Integer, primary_key=True, index=True)
    place = Column(String)


class User(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    addresses: RelationshipProperty = relationship("Address", secondary=address_users, backref="users")
