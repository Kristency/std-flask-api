from db import db
import enum


class MenuItemTypeEnum(enum.Enum):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'


class MenuItem(db.Model):
    __tablename__ = 'menuitems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    type = db.Column(db.Enum(MenuItemTypeEnum))

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def to_json(self):
        return {'name': self.name, 'type': self.type.value}
