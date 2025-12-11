from dice import boarddice, fightdice
import time
def boardplay(answer) :
  board_dice = boarddice.BoardDice()
  if answer == 'Y':
    print('\n\n\n주사위를 굴립니다',end = '')
    time.sleep(1.5)
    print('.',end = ' ')
    time.sleep(1.5)
    print('.',end = ' ')
    time.sleep(1.5)
    print('.\n\n\n')
    time.sleep(1.2)
    diced_num = board_dice.roll()
    return diced_num
  elif answer == 'N' :
    print("아직 마음의 준비가 필요하신가보군요..\n\n")
    time.sleep(1.5)
    print('\n\n잠시 후, 다시 물어보겠습니다...')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('마음의 준비가 다 되셨나요, 다시 물어보겠습니다.\n')
    time.sleep(1)
    re_answer = input('주사위를 굴리시겠습니까?(Y/N):')
    return boardplay(re_answer)
  else :
    print("\n반사회적이시군요.\n")
    time.sleep(1)
    re_answer = input('주사위를 굴리시겠습니까?(Y/N):')
    return boardplay(re_answer)
  

def fightplay(answer) :
  fight_dice = fightdice.FightDice()
  if answer == 'Y':
    print('\n\n\n주사위를 굴립니다',end = '')
    time.sleep(1.5)
    print('.',end = ' ')
    time.sleep(1.5)
    print('.',end = ' ')
    time.sleep(1.5)
    print('.\n\n\n')
    time.sleep(1.2)
    diced_num = fight_dice.roll()
    return diced_num
  elif answer == 'N' :
    print("아직 마음의 준비가 필요하신가보군요..\n\n")
    time.sleep(1.5)
    print('\n\n잠시 후, 다시 물어보겠습니다...')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('마음의 준비가 다 되셨나요, 다시 물어보겠습니다.')
    time.sleep(1.5)
    re_answer = input('주사위를 굴리시겠습니까?(Y/N):')
    return fightplay(re_answer)
  else :
    print("반사회적이시군요.")
    re_answer = input('주사위를 굴리시겠습니까?(Y/N):')
    return fightplay(re_answer)
