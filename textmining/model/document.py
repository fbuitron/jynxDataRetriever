""" Object that represents a document"""

from .entity import Entity

class Document:
    """A documents attributes that makess it an entity"""

    NUMBER_CSV_COLUMNS = 3

    def __init__(self, doc_id, doc_content, entity_list):
        self.doc_id = doc_id
        self.doc_content = doc_content
        self.entity_list = entity_list

    @staticmethod
    def create_document(doc_csv):
        """Invokes the parser and creates the Document Object"""
        list_doc = list(doc_csv)
        if doc_csv:
            if len(list_doc) == Document.NUMBER_CSV_COLUMNS:
                doc_id = list_doc[0]
                doc_contet = list_doc[1]
                entity_list = list_doc[2]
                entity_list_split = entity_list.replace("[", "").replace("]", "").split(">, ")
                list_entity_obj = []
                for entity_item in entity_list_split:
                    clean_entity = " ".join(entity_item.splitlines())
                    obj_entity = Entity.create_entity(clean_entity)
                    list_entity_obj.append(obj_entity)

                result = Document(doc_id, doc_contet, list_entity_obj)
        return result

