import random
from event import battleevent, bossevent, event, itemevent, minigameevent, noevent
from character import character
class Board:
  """게임 보드판 관리"""

  def __init__(self, row, col, event_list):
    self.row = row
    self.col = col
    self.total_tiles = row * col
    self.events = event_list

  @classmethod
  def make_board(cls, row, col):
    """클래스메소드 : 가로, 세로 입력 : Board 인스턴스 반환
    [섞은 전투 칸, 아이템 칸, 빈칸에 보스 칸까지 추가]"""
    total = row * col
    event_list = []
    tile = [battleevent.BattleEvent(),battleevent.BattleEvent(),itemevent.ItemEvent(), itemevent.ItemEvent(), noevent.NoEvent(),minigameevent.MinigameEvent()]
    for _ in range((total+1)//len(tile)):
      random.shuffle(tile)
      event_list += tile
    event_list = [noevent.NoEvent()] + event_list[:(total-2)] + [bossevent.BossEvent()]
    return cls(row, col, event_list)

  @staticmethod
  def display_help():
    """정적 메소드 : 게임 소개 및 도움말 출력"""
    print("\n=== 게임 규칙 ===")
    print("1. 주사위를 던져 뱀형 보드판을 이동합니다.")
    print("2. '전투 칸'에서는 주사위 기반 전투가 발생합니다.")
    print(f'  2-1. 기본 스텟은 \n       공격력 - 10\n       체력 - 100\n       라이프 - 3 입니다.')
    print('  2-2. 주사위를 굴려 나온 숫자에 따라 이 스텟이 증가할 수도, 감소할 수도 있습니다.')
    print('  2-3. 승리 시, 레벨업을 합니다. 패배 시, 라이프가 1 감소합니다.')
    print("3. '아이템 칸'에서는 주사위 관련 아이템을 획득할 수 있습니다.")
    print('4. "미니게임 칸"에서는 라이프 회복 또는 랜덤 아이템을 획득할 수 있습니다.')
    print('5. 라이프가 0이 되면 게임이 종료됩니다.')
    print("6. 보드판의 마지막 칸에 도착하여 보스를 물리치면 승리합니다.\n")
    

  def get_event(self, idx):
    """인덱스 입력 : 이벤트 반환"""
    try:
      event = self.events[idx]
      return event
    except IndexError as e:
      print(f"에러: 보드판 인덱스 {idx}(은)는 범위를 벗어났습니다. <{e}>")
      return noevent.NoEvent()

  def display(self, player_pos):
    """"플레이어 위치 입력 : 보드판 출력"""
    print("\n=== Bansawee ===\n")

    for r in range(self.row):

        start_idx = r * self.col
        end_idx = start_idx + self.col
        if r%2 == 0:
          indices = range(start_idx, end_idx)
        else:
          indices = range(end_idx-1, start_idx-1, -1)

        row_output = []
        for idx in indices:
          event_name = self.events[idx].get_display_name()
          if idx == player_pos:
            display_cell = event_name.replace(']', '(🦸)]')
          else:
            display_cell = event_name
          row_output.append(display_cell)

        print("     ".join(row_output))
        print()
        if r%2: print(' '*14 + '🌲🌳'*5*(self.col-1))
        else:   print('🌲🌳'*5*(self.col-1))
        print()