#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete",
                            backref="place")
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False, backref='place_amenities')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Return all the cities associated with the state"""
            from models import storage
            review_objects = storage.all(Review)
            return [review for review in review_objects.values()
                    if review.place_id == self.id]

        @property
        def amenities(Self):
            """Return all the amenities associated with the place"""
            amenity_objects = storage.all(Amenity)
            return [amenity for amenity in amenity_objects
                    if amenity.id in amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Set all the amenities associated with the place"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenities_ids.append(obj.id)
