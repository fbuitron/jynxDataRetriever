
import textmining.model.document as model
import textmining.serializer.serialize as serializer
import textmining.processing as processing
import textmining.model.document as Document

import csv
import sys


def test_entity_extraction():
    """Test first execution"""

    doc1 = Document.Document("A1", """It was November. Although it was not yet late, the sky was dark when I turned into Laundress Passage. Father had finished for the day, switched off the shop lights and closed the shutters; but so I would not come home to darkness he had left on the light over the stairs to the flat. Through the glass in the door it cast a foolscap rectangle of paleness onto the wet pavement, and it was while I was standing in that rectangle, about to turn my key in the door, that I first saw the letter. Another white rectangle, it was on the fifth step from the bottom, where I couldn't miss it.""", None)
    
    doc2 = Document.Document("B2", """I closed the door and put the shop key in its usual place behind Bailey's Advanced Principles of Geometry. Poor Bailey. No one has wanted his fat gray book for thirty years. Sometimes I wonder what he makes of his role as guardian of the bookshop keys. I don't suppose it's the destiny he had in mind for the masterwork that he spent two decades writing.""", None)
    
    doc3 = Document.Document("C3", """I opened the letter and pulled out a sheaf of half a dozen pages, all written in the same laborious script. Thanks to my work, I am experienced in the reading of difficult manuscripts. There is no great secret to it. Patience and practice are all that is required. That and the willingness to cultivate an inner eye. When you read a manuscript that has been damaged by water, fire, light or just the passing of the years, your eye needs to study not just the shape of the letters but other marks of production. The speed of the pen. The pressure of the hand on the page. Breaks and releases in the flow. You must relax. Think of nothing. Until you wake into a dream where you are at once a pen flying over vellum and the vellum itself with the touch of ink tickling your surface. Then you can read it. The intention of the writer, his thoughts, his hesitations, his longings and his meaning. You can read as clearly as if you were the very candlelight illuminating the page as the pen speeds over it.""", None)

    doc_list = []
    doc_list.append(doc1)
    doc_list.append(doc2)
    doc_list.append(doc3)

    for doc in doc_list:
        entities = processing.startProcessing(doc)
        for entity in entities:
            print(entity)

print("Executing")
firts_execution()
# search()
