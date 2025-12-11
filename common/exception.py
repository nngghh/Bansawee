from dice import dice,boarddice,fightdice
import random, time
class NotValidSelectItem(Exception) :
  def __init__(self) :
    super().__init__('아이템 입력이 올바르지 않습니다.')

def valid_select_item(comm,valid_acquire_item_list) :
  """선택한 아이템(comm)이 얻을 수 있는 아이템 리스트 중에 존재하는지"""
  comm_digit = comm.isdigit() # 들어온 comm이 숫자 텍스트인지 그냥 텍스인지
  try :
    if comm_digit == True :
      if int(comm) not in [i for i in range(1,len(valid_acquire_item_list)+1)]  :
        raise NotValidSelectItem
    else :
      if comm not in valid_acquire_item_list :
        raise NotValidSelectItem
  except Exception as e :
    print(e)
    re_comm = input('획득할 아이템의 이름 또는 번호를 입력해주세요(위에서부터 1번): ')
    return valid_select_item(re_comm,valid_acquire_item_list)
  else :
    if comm.isdigit() :
      return valid_acquire_item_list[int(comm)-1]
    else :
      return comm


class NotValidSelectItem(Exception) :
  def __init__(self) :
    super().__init__('아이템 입력이 올바르지 않습니다.')

def valid_select_item(comm,valid_acquire_item_list) :
  """선택한 아이템(comm)이 얻을 수 있는 아이템 리스트 중에 존재하는지"""
  comm_digit = comm.isdigit() # 들어온 comm이 숫자 텍스트인지 그냥 텍스인지
  try :
    if comm_digit == True :
      if int(comm) not in [i for i in range(1,len(valid_acquire_item_list)+1)]  :
        raise NotValidSelectItem
    else :
      if comm not in valid_acquire_item_list :
        raise NotValidSelectItem
  except Exception as e :
    print(e)
    re_comm = input('획득할 아이템의 이름 또는 번호를 입력해주세요(위에서부터 1번): ')
    return valid_select_item(re_comm,valid_acquire_item_list)
  else :
    if comm.isdigit() :
      return valid_acquire_item_list[int(comm)-1]
    else :
      return comm


class NotHaveItem(Exception) :
  def __init__(self) :
    super().__init__('해당 아이템을 소지하고 있지 않습니다.')

def not_have_item(item,character) :
  try :
    if (item.isdigit() == False and item not in character.acquired_item) or (item.isdigit() == True and int(item) not in [i+1 for i in range(len(character.acquired_item))]):
      raise NotHaveItem # 위에서 지정한 예외를 넣어주자.

  except Exception as e :
    print(e)
    re_item = input('사용할 아이템을 입력해주세요: ')
    return not_have_item(re_item,character)

  else :
    if item.isdigit() == False :
      return item         
    elif item.isdigit() == True :
      return character.acquired_item[int(item)-1]

def will_use_item(answer,character) :
  m = ['\n잉? 가진 게 없는디요?\n','\n이 게임 처음이신가요?\n','\n아~ 잘몯 적으신거죠? 저도 잘몿 적어봤어요~\n','\n가진 아이템이 없는데..무슨...\n']
  board_dice = boarddice.BoardDice()
  if answer == 'Y':
    if character.acquired_item == [] :
      print(random.choice(m))
      time.sleep(1.5)
      return 'None'
    print('\n-------현재 소지하고 있는 아이템-------\n')
    for i in character.acquired_item :
      print(i)
    print()
    use_item_name = input('사용할 아이템을 입력해주세요(아이템 이름 또는 위에서부터 1번): ')
    using_item = not_have_item(use_item_name,character)
    return using_item
  elif answer == 'N' :
    print('행운을 빕니다.')
    return 'None'
  else :
    print("몬스터가 지루해서 떠나버렸습니다...")
    time.sleep(2)
    print('\n라고 할 뻔')
    time.sleep(0.8)
    re_answer = input('\n사용할 아이템을 입력해주세요: ')
    return will_use_item(re_answer,character)