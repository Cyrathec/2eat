from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


class Sport(Base):
    __tablename__ = 'sports'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    # Sport is unique in database
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(512), nullable=True)
    people = relationship("SportAssociation", back_populates="sport")

    def __repr__(self):
        return "<Sport %s>" % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


class SportAssociation(Base):
    """
    Association class between person and sport
    help relationship: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
    """
    __tablename__ = 'sport_associations'
    __table_args__ = (UniqueConstraint('person_id', 'sport_id'),)

    person_id = Column(String(36), ForeignKey('people.id'), primary_key=True)
    sport_id = Column(String(36), ForeignKey('sports.id'), primary_key=True)
    level = Column(String(50))
    person = relationship("Person", back_populates="sports")
    sport = relationship("Sport", back_populates="people")
