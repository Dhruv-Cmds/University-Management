import enum

class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"