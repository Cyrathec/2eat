from model.mapping import Base
import uuid

from sqlalchemy import Column, String, Integer


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    street = Column(String(256), nullable=False)
    city = Column(String(50), nullable=False)
    postal_code = Column(Integer(), nullable=False)
    country = Column(String(50), nullable=False, default="FRANCE")

    def __repr__(self):
        return "<Address(%s, %d, %s %s)>" % (self.street, self.postal_code, self.city, self.country.upper())

    def to_dict(self):
        return {
            "id": self.id,
            "street": self.street,
            "city": self.city,
            "postal_code": self.postal_code,
            "country": self.country
        }
