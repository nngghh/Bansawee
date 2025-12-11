import random
class Dice :
  def __init__(self, faces = 6) :
    '''주사위의 기본적인 속성 메소드'''
    self.faces = faces

  def roll(self) :
    '''주사위를 굴리는 메소드'''
    current_dice = [i for i in range(1,self.faces+1)]
    diced_num = random.choice(current_dice)
    print(f'굴려서 나온 주사위의 숫자는 {diced_num}입니다!')
    return diced_num

  @classmethod
  def faces_20(cls, faces = 20) :
    """20면 주사위를 만드는 클래스메소드"""
    return cls(faces)