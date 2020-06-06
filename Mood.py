class Mood(object):

    def __init__(self, stability, HMULT, SMULT):
        self.stability = stability
        self.HMULT = HMULT
        self.SMULT = SMULT
        
class Happy(Mood):
    def __init__(self):
        super(Happy, self).__init__(1, 1.75, 1)
        
class Angry(Mood):
    def __init__(self):
        super(Angry, self).__init__(1, 0.75, 1.25)
        
class Stressed(Mood):
    def __init__(self):
        super(Stressed, self).__init__(1, 0.5, 1.75)
        
class Sad(Mood):   
    def __init__(self):
        super(Sad, self).__init__(1, 1, 1.75)