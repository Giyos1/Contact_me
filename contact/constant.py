from enum import Enum


class NumberType(Enum):
    MOBILE = 'Mobile'
    HOME = 'Home'
    EMAIL = 'Email'
    ADDRESS = 'Address'
    OTHER = 'Other'

    @classmethod
    def choice(cls):
        return ((i.name, i.value) for i in cls)
