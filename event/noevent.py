from event import event
import random, time
class NoEvent(event.Event):
  """빈칸 이벤트"""
  @staticmethod
  def start(player):
    comments = {'게임 만드는 거 너무 힘들었어요 ㅠㅠ':'\n', '사실 보스가 제일 쉬워요':'높은 숫자가 나온다면요~\n',
                '왜 똑같은 나무만 있는지 궁금하지 않나요?':'딱히 이유는 없어요, 애초에 있겠나요..?\n','사실 보드판은 처음에 나선형으로 계획되었답니다.':'근데 너무 머리 아팠어요.\n',
                '수상한 사람 말은 믿지 않는 것이 좋아요...':'평범인은 믿을 만합니다.\n','즐거운 크리스마스 되세요~':'새해 복 많이 받으세요~',
                '게임 이름이 왜 반사위인지 궁금하지 않나요?':'안 궁금하셔도 들으세요.\n처음이게임을만들었을때전부다주사위로만진행되는\n아주아주도박과도파민을추구하는그런반사회적인게임이라고생각해서\n주사위와반사회적인이라는말을섞어서언어유희처럼반사위라고지었습니다.'
                ,'혹시 같은 칸이 연속해서 나오나요..?':'어쩔 수 없어요.. 랜덤이라서요..','혹시 아까 전에도 여기 왔었나요..?':'운이 좀 많이 없으신듯 하네용ㅋ'}
    print('잠시 쉬어가는 시간~')
    for i in range(3) :
      time.sleep(1.5)
      print('.')
      print()
    time.sleep(1.5)
    print('\n재밌는 얘기 해드릴까요?')
    for i in range(3) :
      time.sleep(1.5)
      print('.')
      print()
    time.sleep(1.5)
    comment_key = random.choice(list(comments.keys()))
    comment_value = comments[comment_key]
    print(comment_key)
    time.sleep(4)
    print(comment_value)
    time.sleep(2)

  def get_display_name(self):
    return '[ 🍃 빈칸 🍃 ]'