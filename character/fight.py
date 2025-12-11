import random, time
from character import character, fight, monster
class Fight(character.Character):
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster

    def hero_attack(self):
        c = ['ca','ca','','','','','','','','']
        if self.hero.roll == 2 :
            for i in range(self.hero.roll-1) :
                c[i] = ''
        elif self.hero.roll <= 1 :
            for i in range(len(c)) :
                c[i] = ''
        elif self.hero.roll >= 4 :
            for i in range(self.hero.roll) :
                c[i] = 'ca'
        is_c = random.choice(c)
        if is_c == 'ca' :
            dmg = self.hero.ap * 2
            self.monster.hp -= dmg
            if self.monster.hp < 0 : self.monster.hp = 0
            print(f"{self.hero.char_name} (이)가 {self.monster.char_name}에게 {dmg} 크리티컬 피해를 주었다! "
                f"(몬스터 체력: {self.monster.hp})")
        else :
            dmg = self.hero.ap
            self.monster.hp -= dmg
            if self.monster.hp < 0 : self.monster.hp = 0
            print(f"{self.hero.char_name} (이)가 {self.monster.char_name}에게 {dmg} 피해를 주었다! "
                f"(몬스터 체력: {self.monster.hp})")

    def monster_attack(self):
        c = ['ca','ca','','','','','','','','']
        is_c = random.choice(c)
        if is_c == 'ca' :
            dmg = self.monster.ap * 2
            self.hero.hp -= dmg
            if self.hero.hp < 0 : self.hero.hp = 0
            print(f"{self.monster.char_name} (이)가 {self.hero.char_name}에게 {dmg} 크리티컬 피해를 주었다! "
              f"(영웅 체력: {self.hero.hp})")
        else :
            dmg = self.monster.ap
            self.hero.hp -= dmg
            if self.hero.hp < 0 : self.hero.hp = 0
            print(f"{self.monster.char_name} (이)가 {self.hero.char_name}에게 {dmg} 피해를 주었다! "
                f"(영웅 체력: {self.hero.hp})")


    def battle(self):
        c_a = self.hero.ap
        c_h = self.hero.hp
        print("\n===== 전투 시작 =====")
        print(f"{self.hero.char_name}        vs         {self.monster.char_name}")
        print(f'공격력 - {self.hero.ap}            공격력 - {self.monster.ap}')
        print(f'체력 - {self.hero.hp}          체력 - {self.monster.hp}')
        turn = 1
        while self.hero.hp > 0 and self.monster.hp > 0:
            print(f"\n--- {turn} 턴 ---")
            self.hero_attack()

            if self.monster.hp <= 0:
                self.hero.levelup()
                print(f"\n승리!, 레벨 1 상승\n ")
                print()
                time.sleep(1)
                print(f'공격력 10 상승!')
                time.sleep(1)
                print(f'체력 100 상승!')
                # self.hero.hp = 100 * character.Character.levelhp
                break

            self.monster_attack()
            time.sleep(1.5)
            print()

            if self.hero.hp <= 0:
                # self.hero.levelup()
                print(f"\n전투 패배..")
                time.sleep(1.5)
                print('\n라이프 1 감소')
                time.sleep(1.5)
                self.hero.life-=1  #라이프 전달받아야 함
                print('남은 라이프 {}'.format(self.hero.life))
                # self.hero.hp =100 * character.Character.levelhp
                break

            turn += 1