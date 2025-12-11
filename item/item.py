import time
import random
from dice import dice, boarddice, fightdice
from common import exception, play
from character import character, fight, monster
class Item :

  item_dic = {'1나오면 다시 굴리기':'주사위를 굴려서 1이 나오면 1을 제외하고 다시 굴립니다.','나온 숫자 2배':"주사위를 굴려서 나온 숫자가 2배가 됩니다.",
               '특별 20면 주사위':'☞☞*%%특별 20면 주사위%%*☜☜','나온 숫자 +1':'주사위를 굴려서 나온 숫자가 +1 됩니다.'}
  
  gamble_num = []
  def __init__(self,item_name) :
    self.item_name = item_name

  @staticmethod
  def use(item_name,character) :     
    if item_name == '1나오면 다시 굴리기' and Item.valid_item(item_name,character) :
      answer = input('주사위를 굴리시겠습니까?(Y/N):')
      diced_num = play.fightplay(answer)
      print(f'굴려서 나온 주사위의 숫자는 {diced_num}입니다.')
      time.sleep(1)
      if diced_num == 1 :
        print('1이 나와서 다시 굴리겠습니다!')
        time.sleep(1.5)
        diced_num = random.choice([2,3,4,5,6])
        print(f'다시 굴려서 나온 주사위의 숫자는 {diced_num}입니다.')
      return diced_num

    if item_name == '나온 숫자 2배' and Item.valid_item(item_name,character) :
      answer = input('주사위를 굴리시겠습니까?(Y/N):')
      diced_num = play.fightplay(answer)
      final_num = diced_num * 2
      print(f'굴려서 나온 주사위의 숫자 {diced_num}(이)가 {final_num}(으)로 2배가 됩니다.')
      return final_num

    if item_name == '특별 20면 주사위' and Item.valid_item(item_name,character) :
      dice_20 = dice.Dice.faces_20()
      print('(ง •̀ω•́)ง, ٩(๑′∀ ‵๑)۶•¨•.¸¸♪, (´▽`ʃ♡ƪ) ~~~특별 20면 주사위가 굴러갑니다~~~ (ﾟ´ωﾟ)ﾟ｡｡ﾟ(ﾟ´ωﾟ)ﾟ｡ (∩´∀`∩)☆')
      time.sleep(3)
      diced_num = dice_20.roll()
      return diced_num

    if item_name == '나온 숫자 +1' and Item.valid_item(item_name, character) :
      answer = input('주사위를 굴리시겠습니까?(Y/N):')
      diced_num = play.fightplay(answer)
      plus_num = diced_num + 1
      print(f'굴려서 나온 주사위의 숫자 {diced_num}(이)가 +1 되어 {plus_num}(으)로 됩니다.')
      return plus_num

    for i in Item.gamble_num :
      if item_name == f'도박 주사위(+{i[0]}/-{i[1]})' and Item.valid_item(item_name,character) :
        appear = ['O','X']
        is_appear = random.choice(appear)

        if is_appear == 'O' :
          print()
          hangin = random.choice([1,2,3,4,5,6])
          time.sleep(1.5)
          print(f'수상한 평범인 : ??')
          time.sleep(1.5)
          print()
          print(f'수상한 평범인 : 거.. 도박해유?')
          time.sleep(1.5)
          print()
          print(f'수상한 평범인 : 아 뭔가 {hangin} 나올 거 같은데..~')
          time.sleep(1.5)
        else :
          time.sleep(1.5)
        while True:
          pred_num = input('\n주사위를 굴리기 전~! 어떤 숫자가 나올까요~~?(1~6): ')
          if pred_num.isdigit() == False or (pred_num.isdigit() == True and int(pred_num) not in [i for i in range(1,7)]) :
            print('\n에이~ 도박을 시작할 땐 맘대로지만 나갈 땐 아니잖아요~?')
          else :
            break
        print('\n자~ 과연 맞는지 볼까요? 두구두구~~')
        time.sleep(1)
        print()
        diced_num = play.fightplay('Y')
        if diced_num == int(pred_num) :
          time.sleep(1.5)
          result_num = diced_num + i[0]
          print('\n운이 정말 좋네요..')
          time.sleep(1.3)
          print(f'\n도박에 성공해서 {i[0]}을(를) 더해 {result_num}가 됩니다...')
          time.sleep(3)
          if is_appear == 'O' and hangin == pred_num :
            print('수상한 평범인 : 이게 왜 진짜 나오냐....')
          time.sleep(3)
        elif diced_num != int(pred_num) :
          result_num = diced_num - i[1]
          time.sleep(1.5)
          print('\n어머 어떡행.. ', end = '')
          time.sleep(1.5)
          print('아~',end = '')
          time.sleep(0.5)
          print('쉽~', end = '')
          time.sleep(0.5)
          print('게~', end = '')
          time.sleep(0.5)
          print('도~ ', end = '')
          time.sleep(1.3)
          print('틀려 버렸네용..',end = ' ')
          time.sleep(1.5)
          print('으잉 ㅠㅠ 제가 다 슬프네용 ㅠㅠㅠ 8ㅅ8')
          time.sleep(1.5)
          print(f'\n도박에 ""실패""하셔서~ {i[1]}을(를) ""깍아서"" {result_num}(이)가 되어버렸습니당~~!')
          time.sleep(1.5)
          if result_num < 0 :
            result_num = 0
            print("아~ 근데 아무래도 마이너스는 너무 마음이 아프니까~\n")
            time.sleep(1.5)
            print('특!',end=' ')
            time.sleep(1)
            print('별!',end=' ')
            time.sleep(1)
            print('히!',end=' ')
            time.sleep(1.5)
            print(f'{result_num}으로 해드릴게요~~\n')
          if is_appear == 'O':
            print('수상한 평범인 : ㅎㅎ (홀연히 사라졌다.)')
          time.sleep(3)
        return result_num

    else :
      item_name = input('사용할 아이템을 입력해주세요: ')
      Item.use(item_name,character)

  @staticmethod
  def valid_item(item_name,character) :
    have_item = item_name in character.acquired_item  # 캐릭터의 아이템 리스트에 아이템 이름이 있는지 (변경해야함)
    exist_item = item_name in Item.item_dic
    is_all_true = (exist_item == True and have_item == True)
    return is_all_true