
from sqlalchemy import Column, Boolean, String, ForeignKey
from model.mapping.person import Person


class Member(Person):
    __tablename__ = 'members'

    id = Column(String(36), ForeignKey('people.id'), primary_key=True)
    medical_certificate = Column(Boolean(), nullable=False, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'member',
    }

    def __repr__(self):
        return "<Member(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        _dict = super().to_dict()
        _dict['medical_certificate'] = self.medical_certificate
        return _dict
