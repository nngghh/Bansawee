from character import character
import random
class Monster(character.Character):
  @staticmethod
  def get_random_scale():
    return random.randrange(90,111) * 0.01

  def __init__(self, mon_name):
      super().__init__(mon_name)
      scale = Monster.get_random_scale()
      self.hp = int((self.hp * scale))
      self.ap = int(self.ap * scale)
      if mon_name == '스톤 골렘':
        self.hp=self.hp * 3
      elif mon_name =='오크 전사':
        self.hp*=2
        self.ap*=1.5
      elif mon_name =='불의 정령':
        self.hp*=0.9
        self.ap*=1.4
      elif mon_name =='드레곤':
        self.ap*=2
        self.hp*=2
  @classmethod
  def make_char(cls,mon_name):
    return cls(mon_name)