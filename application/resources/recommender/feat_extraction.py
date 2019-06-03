

class User:
    def __init__(self, org={}):
        self.word = org['word']
        self.category = org['category']
        self.word_s1 = org['word_s1']
        self.word_s2 = org['word_s2']
        self.word_s3 = org['word_s3']
        self.word_s4 = org['word_s4']
        self.phase = org['phase']
        self.primary_syllable_stress = org['primary_syllable_stress']

    def preProcessing(self):
        sampleString = self.__dict__
        for key, value in list(sampleString.items()):
            if value == 'string' or value == '':
                del sampleString[key]
        return sampleString
