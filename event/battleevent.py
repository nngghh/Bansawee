import random
from item import item
from character import monster, fight, fightcharacter
from event import event
from common import exception, play
class BattleEvent(event.Event):
  """전투 칸 이벤트"""
  @staticmethod
  def start(player):
    mon_list = ['슬라임', '고블린', '곰', '오크 마법사', '스켈레톤', '늑대', '스톤 골렘', '불의 정령']
    mon_name = random.choice(mon_list)
    selected_monster = monster.Monster.make_char(mon_name)
    print(f"{selected_monster}\n이(가) 등장했습니다! 바로 전투로 들어갑니다.\n")

    use_item_select = input('아이템을 사용하시겠습니까?(Y/N): ')
    used_item = exception.will_use_item(use_item_select,player)
    if used_item == 'None' :
      answer = input('주사위를 굴리시겠습니까?(Y/N):')
      fight_num = play.fightplay(answer)
    elif used_item != 'None' :
      fight_num = item.Item.use(used_item,player)
      player.acquired_item.remove(used_item)
    if used_item == '특별 20면 주사위' :
      if fight_num <= 9 :
        print(f'나온 숫자 {fight_num}만큼 공격력과 체력이 감소합니다..')

      elif fight_num == 10 :
        print(f'나온 숫자가 {fight_num}이므로 기본 스텟이 유지됩니다.')

      elif fight_num >= 11 :
        print(f'나온 숫자 {fight_num}만큼 공격력과 체력이 증가합니다!')
    else :
      if fight_num <= 2 :
        print(f'나온 숫자 {fight_num}만큼 공격력과 체력이 감소합니다..')

      elif fight_num == 3 :
        print(f'나온 숫자가 {fight_num}이므로 기본 스텟이 유지됩니다.')

      elif fight_num >= 4 :
        print(f'나온 숫자 {fight_num}만큼 공격력과 체력이 증가합니다!')

    p_n, p_h, p_a, p_l, p_i = player.char_name, player.hp, player.ap, player.life, player.acquired_item
    fightchar = fightcharacter.FightCharacter(fight_num,p_n,p_h,p_a,p_l,used_item,p_i)
    game = fight.Fight(fightchar, selected_monster)
    game.battle()
  def get_display_name(self):
    return '[ ⚔️ 전투 ⚔️ ]'