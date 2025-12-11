from event import event
from item import item
from common import exception
import time, random
class ItemEvent(event.Event):
  """아이템 칸 이벤트"""
  @staticmethod
  def start(player):
    a = [2,3,4]
    b = [1,2]
    r_n1 = random.choice(a)
    r_n2 = random.choice(b)
    if [r_n1,r_n2] not in item.Item.gamble_num :
      item.Item.gamble_num.append([r_n1,r_n2])
      it = {f'도박 주사위(+{r_n1}/-{r_n2})':f'나올 숫자를 맞히면 +{r_n1}, 틀리면 -{r_n2}가 됩니다.'}
      item.Item.item_dic[f'도박 주사위(+{r_n1}/-{r_n2})'] = it[f'도박 주사위(+{r_n1}/-{r_n2})']
    else :
      pass

    valid_acquire_item = random.sample(list(item.Item.item_dic.keys()),k=3)
    print('~획득 가능한 아이템~\n')
    i_list = []
    for i in valid_acquire_item :
      time.sleep(1)
      print(f"➡ {i} - {item.Item.item_dic[i]}", end = '\n\n')
      i_list.append(i)
    time.sleep(1.3)
    select = input('획득할 아이템의 이름 또는 번호를 입력해주세요(위에서부터 1번): ')
    selected_item = exception.valid_select_item(select, i_list)
    player.acquired_item.append(selected_item)
    print(f'"{selected_item}"를 획득했습니다!')
  def get_display_name(self):
    return '[💎 아이템 💎]'