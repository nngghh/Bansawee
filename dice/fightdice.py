from dice import dice
class FightDice(dice.Dice) :
  def __init__(self,faces = 6) :
    self.faces = faces
    super().__init__(faces)