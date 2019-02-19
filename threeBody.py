class ThreeBody:
    def __init__(self):
        self.name = 'ThreeBody'
        self.attributes = {
            'STR':      4,
            'AGI':      4,
            'SMA':      4,
            'SPI':      4,
            'VIG':      4
        }
        self.skills = {
            'Fighting':         4,
            'Notice':           4,
            'CommonKnowledge':  4,
            'Stealth':          4
        }
        self.armor = {
            'Head':     0,
            'Arms':     0,
            'Torso':    0,
            'Legs':     0,
            'Feet':     0
        }

    def baseToughness(self):
        return (self.attributes['VIG']/2)+2

    def toughness(self,position):
        return (self.baseToughness()+self.armor[position])

    def baseParry(self):
        return (self.skills['Fighting']/2)+2
