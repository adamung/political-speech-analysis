class Speech:
    def __init__(self, filename, party, speaker, text, year):
        self.filename = filename
        self.party = party
        self.speaker = speaker
        self.text = text
        self.year = year
        self.vector_doc2vec = None
        self.vector_bert = None

    def get_party(self):
        return self.party

    def get_year(self):
        return self.year

    def get_speaker(self):
        return self.ledamot

    def get_text(self):
        return self.text
    
    def get_vector_doc2vec(self):
        return self.vector_doc2vec
    
    def get_vector_bert(self):
        return self.vector_bert
    
    def set_vector_doc2vec(self, vector):
        self.vector_doc2vec = vector

    def set_vector_bert(self, vector):
        self.vector_bert = vector
