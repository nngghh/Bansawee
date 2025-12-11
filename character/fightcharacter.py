from character.character import Character
from common import play
class FightCharacter(Character):
  def __init__(self, roll, player, used_item):
    self.player = player
    self.hp = player.hp
    self.ap = player.ap
    self.char_name = player.char_name
    self.life = player.life
    self.used_item = used_item
    self.roll = roll
    self.acquired_item = player.acquired_item
    n = {9:12,8:13,7:14,6:15,5:16,4:17,3:18,2:19,1:20,0:20}
    if self.used_item == '특별 20면 주사위' :
      if self.roll >= 11 :
        self.hp += self.roll * 10
        self.ap += self.roll * 2
      elif self.roll <= 9 :
        self.hp -= n[self.roll] * 10 * 0.25
        self.ap -= n[self.roll] * 2 * 0.25
    
    else :
      a = {1:6,2:5,0:6}
      if self.roll <=2:
        self.hp -= a[self.roll] * 10
        self.ap -= a[self.roll]* 2 * 0.5
      elif roll >=4:

        self.hp += self.roll * 10
        self.ap += self.roll * 2
  def life_down(self) :
    self.player.life -= 1










