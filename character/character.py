class Character:
  level=1
  levelhp=1
  levelap=1
  def __init__(self,char_name):
    self.char_name=char_name
    self.level = 1
    self.max_hp = 100 * self.level
    self.hp=self.max_hp
    self.ap=10*self.level
    self.life=3
    self.acquired_item = []
  def apply_level(self):
    self.max_hp = 100 * Character.levelhp
    self.hp =self.max_hp 
    self.ap = 10 * Character.levelap

  @classmethod
  def make_char(cls,char_name) :
    return cls(char_name)
  def __str__(self):
    return (f'''{self.char_name}
체력 - {self.hp}
# 공격력 - {self.ap}''')
  def levelup(self):
    self.level += 1
    self.__init__(self.char_name)