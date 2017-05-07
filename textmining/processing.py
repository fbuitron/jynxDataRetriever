""" Placeholder module where we include all the processing done to a text file """

import nltk
from collections import defaultdict
from .model.document import Document
from .serializer import serialize

doc_path = 'output/documents/'
index_path = 'output/indexes/'

entity_index_file_name = 'entity_index.p'

positional_index_file_name = 'positional_index.p'


# Had to do this to be able to pickle the Index
def lambda_default_dict():
    return defaultdict(list)

positional_index = defaultdict(lambda_default_dict)
entity_index = defaultdict(list)


def store_doc(doc):
    doc_file_name = doc.doc_id + '.p'
    serialize.dump_object(doc, doc_path, doc_file_name)

def retrieve_entity_names(sample_text):
    sentences = nltk.sent_tokenize(sample_text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]    
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    entity_names = []
    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)
        # print(extract_entity_names(tree))
        entity_names.extend(extract_entity_names(tree))

    return set(entity_names)

def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names

def build_entity_index(doc, entities):
    for named_entity in entities:
        entity_index[named_entity].append(doc.doc_id)
    return entity_index


def build_positional_index(doc):
    sentences = nltk.sent_tokenize(doc.doc_content)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    token_position = 0
    for token_sent in tokenized_sentences:
        # one iteration per sentences
        for token in token_sent:
            # one iteration per token
            positional_index[token][doc.doc_id].append(token_position)
            token_position = token_position + 1

    # print('Positional Index')
    # print(positional_index)
    
def storeIndex():
    # print(entity_index.items())
    serialize.dump_object(positional_index, index_path, positional_index_file_name)
    serialize.dump_object(entity_index, index_path, entity_index_file_name)

def recoverIndex():
    entity_index = serialize.get_object(index_path, entity_index_file_name)

def print_index():
    # print(entity_index.items())
    print("A")

def startProcessing(doc=None):
    """ Begin of processing for doc or test if not """

    print("Processing Document: ",doc.doc_id)
    # Stores the document object into disk
    store_doc(doc)

    # Extract entities from Document
    entities = retrieve_entity_names(doc.doc_content)
    
    return entities

    # Build Entity Index: This is touching the general entity
    # build_entity_index(doc, entities)

    # Build Positional Index
    # build_positional_index(doc)



def search_tokens(search_term):
    # retrieve the positional index from disk
    positional_index = serialize.get_object(index_path, positional_index_file_name)
    entity_index = serialize.get_object(index_path, entity_index_file_name)

    # Should be the same index!
    if entity_index[search_term]:
        for documents_pos in entity_index[search_term]:
            print(documents_pos)
    else :
        if positional_index[search_term]:
            # the term exists
            for documents_pos in positional_index[search_term]:
                print(documents_pos)
        else:
            # none
            print("No results for ",search_term)





'''
1. Put the document on a Pickle and put it on the Disk: DONE
2. Extract Entities: DONE
3. Build the Entity Index (No position yet): DONE
4. Build the Token Index (With Position): DONE
5. Create the Flask app and query a String and return the document id 
6. Index can and should go on a pickle as well
7. The data structure of the picke do we use defaultDict? Looks like defaultDict is the best structure to store the index

For the UI
1. How we are going to show the Search
2. How we are going to show the results
3. Building a Table? (?) The IR book has sth here we can iterate.
'''