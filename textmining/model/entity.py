""" Object that represents an entity"""


class Entity:
    """A documents attributes that makess it an entity"""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_entity(entity_text):
        """Creates an entity out of the <Entity: Name> string"""
        entity_split = entity_text.split(":")
        if len(entity_split) > 0:
            entity_name = entity_split[0].replace(">", "")
            return Entity(entity_name)

