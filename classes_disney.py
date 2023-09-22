class Person:

    def __init__(self, name, hair, eye, skin, facial_hair, elderly, glasses, pony_tail, big_nose,hats, earring):
        self.name = name
        self.hair = hair
        self.eye = eye
        self.skin = skin
        self.facial_hair = facial_hair
        self.elderly = elderly
        self.glasses = glasses
        self.pony_tail = pony_tail
        self.big_nose = big_nose
        self.hats = hats
        self.earring = earring


    def __str__(self):
        return 'Name  {}, hair {}, eye {}, skin {}, facial hair {},elderly {},glasses {},pony tail {},big nose {},hats {},earring {}'.format(self.name, self.hair, self.eye, self.skin,self.facial_hair,self.elderly,self.glasses,self.pony_tail,self.big_nose,self.hats,self.earring)
