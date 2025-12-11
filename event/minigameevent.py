from event import event
from item import item
import random, time

class MinigameEvent(event.Event):
  GAMES = ['가위바위보', '홀짝 맞추기', '숫자 야구', '업다운']

  def __init__(self):
    self.win = False
    return super().__init__()

  def start(self, player):
    self.game = random.choice(MinigameEvent.GAMES)
    self.play(self.game)
    if self.win:
      if self.game in ['가위바위보', '홀짝 맞추기']:
        if player.life == 5 :print('최대 추가 라이프 5를 넘을 수 없습니다.')
        elif player.life < 5 :
          player.life += 1
          if player.life <3 :
            print('라이프가 1 회복되었습니다!')
          elif player.life == 3 :
            print('추가 라이프 1 회복되었습니다!')
      elif self.game in ['숫자 야구', '업다운']:
        ran_item = random.choice([i for i in item.Item.item_dic.keys()])
        player.acquired_item.append(ran_item)
        print(f'{ran_item}을 획득했습니다!')
        pass
    return super().start(player)

  def rps(self):
    self.win = None
    while self.win == None :
      option = ['가위', '바위', '보']
      com = random.choice(option)
      user = input("가위/바위/보 중 하나를 내세요: ").strip()
      while user not in option:      user = input("잘못 입력했습니다!\n가위/바위/보 중 하나를 내세요: ").strip()
      time.sleep(0.5)
      print("가위, 바위 보!")
      time.sleep(1)
      print(f"상대는 {com}를 냈습니다.", end=' ')
      if (com == '가위' and user == '바위') or (com == '바위' and user == '보') or (com == '보' and user == '가위') :      
        self.win = True
      elif (com == user) :
        self.win = None
      else :
        self.win = False
      time.sleep(0.1)
      if self.win:      print("이겼습니다!")
      elif self.win == None:      print('비겼습니다!')
      elif self.win == False : print('졌습니다.')

  def even_odd(self):
    option = ['앞면', '뒷면']
    coin = random.choice(option)
    print("동전을 던졌습니다!")
    time.sleep(0.5)
    guess = input("무슨 면이 나왔을지 맞춰보세요(앞면/뒷면): ").strip()
    while guess not in option:      guess = input("잘못 입력했습니다!\n앞면 또는 뒷면 중 하나를 입력하세요: ").strip()
    time.sleep(0.5)
    if guess == option:
      self.win = True
      print("맞췄습니다!")
    else:
      self.win = False
      print("틀렸습니다...")

  def num_baseball(self):
    dgt = [str(i) for i in range(10)]
    while int(''.join(dgt[:3]))<100:      random.shuffle(dgt)
    num = ''.join(dgt[:3])
    print('10턴만에 맞춰보세요!')
    for turn in range(1,11):
      time.sleep(0.5)
      guess = input("[{}턴]\n세자리 숫자를 맞춰보세요: ".format(turn))
      while len(guess) != 3:       guess = input("세 자리인 숫자를 입력해주세요: ")
      strikes, balls = 0, 0
      for i in range(3):
        if guess[i] == num[i]:        strikes += 1
        elif guess[i] in num:        balls += 1
      time.sleep(0.5)
      print("스트라이크(숫자, 자리 일치): {}, 볼(숫자 일치): {}".format(strikes, balls))
      if strikes == 3:
        self.win = True
        time.sleep(0.5)
        print("{}턴 만에 맞췄습니다!".format(turn))
        break

  def up_down(self):
    answer = random.randint(1,100)
    print('10턴만에 맞춰보세요!')
    for turn in range(1,11):
      time.sleep(0.5)
      guess = int(input(f"[{turn}턴]\n1 이상 100 이하의 숫자를 맞춰보세요: "))
      while (guess<1 or guess>100):       guess = int(input("[오류] 1 이상 100 이하 자연수를 입력해주세요: "))
      time.sleep(0.5)
      if guess == answer:
        self.win = True
        print("{}턴 만에 맞췄습니다!".format(turn))
        break
      elif answer>guess: print("업!")
      elif answer<guess: print("다운!")
    if not self.win:
      print("10턴 종료! 졌습니다. 정답은 {}!".format(answer))

  def play(self, game_type):
    print(game_type, "시작!")
    if game_type == '가위바위보':
      self.rps()
    if game_type == '홀짝 맞추기':
      self.even_odd()
    if game_type == '숫자 야구':
      self.num_baseball()
    if game_type == '업다운':
      self.up_down()

  def get_display_name(self):
    return '[🕹️미니게임🕹️]'