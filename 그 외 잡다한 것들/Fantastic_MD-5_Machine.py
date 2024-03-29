import hashlib
import time
import os
import random as rd

deburf_list = [
    [],
    []
]

magics = [
    ("화염 발사", 1, 150, 10),  # 지속딜
    ("마나 회복", 0, 0),
    ("체력 회복", 0, 0),
    ("회복 마법", 0, 0),
    ("방어 마법", 0, 0),
    ("반사 마법", 2, 0),
    ("번개 마법", 1, 300, 5),
    ("맹독 마법", 1, 500, 4),  # 지속딜
    ("씨발 부활", 0, 0),
    ("각성 마법", 0, 0),
    ("씨발 자폭", 2, 0),  # 현제 자신 체력 - 1의 데미지를 모두에게 부여
    ("저주 마법", 1, 50, 20),  # 지속딜 + 힘 감소
    ("혼란 마법", 0, 0),  # 크리, 중첩 확률 감소
    ("불운 방법", 0, 0),  # 운 감소
    ("흡혈 마법", 2, 0),  # 상대 체력 강탈
    ("마나 흡수", 0, 0)  # 상대 마나 강탈
]


class player:
    def __init__(self):
        self.name = foolish_fun
        self.md5 = foolish_fun
        self.health = 0  # 체력
        self.power = 0  # 힘           : 공격 확률
        self.defence = 0  # 방어          : 데미지 반감 확률
        self.speed = 0  # 회피          : 공격 무효화 확률
        self.luck = 0  # 정확도
        self.mana = 0  # 마나          :
        self.magic = 0  # 마법 강도      : 마법의 세기
        self.magics = []  # 마법 종류
        self.critical = 0  # 크리티컬 확률
        self.critic = 0  # 크리티컬 배수
        self.hit_rate = 0  # 중첩 공격 확률

        self.original_health = 0
        self.original_power = 0
        self.original_defence = 0
        self.original_speed = 0
        self.original_luck = 0
        self.original_mana = 0
        self.original_magic = 0
        self.original_critical = 0
        self.original_critic = 0
        self.original_hit_rate = 0

    def attack(self, ally):
        ply_persent = rd.randrange(1, 1000)
        if self.luck >= ply_persent:
            ply_persent2 = rd.randrange(1, 1000)
            if self.critical >= ply_persent2:
                ply_persent3 = rd.randrange(1, 1000)
                if ally.speed >= ply_persent3:
                    return self.name, "상대의 회피 성공!", 0, ally.name, ally.health / 10
                else:
                    ally.health = ally.health - self.power * self.critic / 1000
                    return self.name, "크리티컬!!", self.power * self.critic / 10000, ally.name, ally.health / 10
            else:
                ply_persent3 = rd.randrange(1, 1000)
                if ally.speed >= ply_persent3:
                    return self.name, "상대의 회피 성공!", 0, ally.name, ally.health / 10
                else:
                    ally.health = ally.health - self.power
                    return self.name, "일반 공격", self.power / 10, ally.name, ally.health / 10
        else:
            return self.name, "공격 실패!", 0, ally.name, ally.health / 10


def typing(strigab, dsv=False):
    for dab in strigab:
        print(dab, end='')
        time.sleep(0.01)
    if dsv:
        print()


def foolish_fun(dsav, da=True):
    dsav = dsav / 10
    if dsav / 100 >= 1:
        return str(dsav)
    else:
        if dsav / 10 >= 1:
            if da:
                return str(' ' + str(dsav))
            else:
                return str(str(dsav) + ' ')
        else:
            if da:
                return str('  ' + str(dsav))
            else:
                return str(str(dsav) + '  ')


def mapping_md5(adbad):
    adbad.md5 = hashlib.md5(adbad.name.encode()).hexdigest()
    adbad.health = int((int(adbad.md5[0] + adbad.md5[1], 16) + 1) * 4000 / 256 + 1000)
    adbad.defence = int((int(adbad.md5[2] + adbad.md5[3], 16) + 1) * 1000 / 256)
    adbad.power = int((int(adbad.md5[4] + adbad.md5[5], 16) + 1) * 1000 / 256)
    adbad.speed = int((int(adbad.md5[6] + adbad.md5[7], 16) + 1) * 700 / 256)
    adbad.luck = int((int(adbad.md5[8] + adbad.md5[9], 16) + 1) * 700 / 256) + 300
    adbad.mana = int((int(adbad.md5[10] + adbad.md5[11], 16) + 1) * 1000 / 256)
    adbad.critical = int((int(adbad.md5[12] + adbad.md5[13], 16) + 1) * 300 / 256)
    adbad.critic = int((int(adbad.md5[14] + adbad.md5[15], 16) + 1) * 8000 / 256) + 2000
    adbad.hit_rate = int((int(adbad.md5[16] + adbad.md5[17], 16) + 1) * 1000 / 256)
    adbad.magic = int((int(adbad.md5[18] + adbad.md5[19], 16) + 1) * 1000 / 256)
    adbad.magics = [int(adbad.md5[20], 16), int(adbad.md5[21], 16), int(adbad.md5[22], 16)]
    adbad.original_health = adbad.health
    adbad.original_power = 0
    adbad.original_defence = 0
    adbad.original_speed = 0
    adbad.original_luck = 0
    adbad.original_mana = 0
    adbad.original_magic = 0
    adbad.original_critical = 0
    adbad.original_critic = 0
    adbad.original_hit_rate = 0


player1 = player()
player2 = player()

typing("Fantastic MD-5 Machine Operating .....\n")
typing("플레이어 1의 이름은 무엇입니까? : ", False)
player1.name = str(input())
typing("플레이어 2의 이름은 무엇입니까? : ", False)
player2.name = str(input())

mapping_md5(player1)
mapping_md5(player2)

os.system('cls')
typing("서로의 스텟")
print("")
print(player1.name + ' vs ' + player2.name)
print("")
print(foolish_fun(player1.health), '|', foolish_fun(player2.health, False), ": 체력")
print(foolish_fun(player1.power), '|', foolish_fun(player2.power, False), ": 힘")
print(foolish_fun(player1.defence), '|', foolish_fun(player2.defence, False), ": 방어")
print(foolish_fun(player1.speed), '|', foolish_fun(player2.speed, False), ": 회피")
print(foolish_fun(player1.luck), '|', foolish_fun(player2.luck, False), ": 운")
print(foolish_fun(player1.mana), '|', foolish_fun(player2.mana, False), ": 마나")
print(foolish_fun(player1.magic), '|', foolish_fun(player2.magic, False), ": 마법 세기")
print(foolish_fun(player1.critical), '|', foolish_fun(player2.critical, False), ": 크리티컬 확률")
print(foolish_fun(player1.critic), '|', foolish_fun(player2.critic, False), ": 크리티컬 배수")
print(foolish_fun(player1.hit_rate), '|', foolish_fun(player2.hit_rate, False), ": 중첩 공격 확률")
time.sleep(4)
print("")
print(player1.name, "의 마법 : ", end='')
for i in player1.magics:
    time.sleep(1)
    print(magics[i], end='. ')
print()
time.sleep(1)
print(player2.name, "의 마법 : ", end='')
for i in player2.magics:
    time.sleep(1)
    print(magics[i], end='. ')
print()  # 맵핑 결과 알려주는 코드... 쓸데없이 길어서 줄임.

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

typing("게임을 시작합니다...")

turn = 1

while True:
    os.system("cls")
    print('%d 번째 턴' % turn)
    print('------------------------------------------')
    attack = player1.attack(player2)
    print('%s의 공격\n %s %d 데미지\n %s의 남은 체력 : %d / %d' % (attack[0],
                                                        attack[1],
                                                        attack[2],
                                                        attack[3],
                                                        attack[4],
                                                        player2.original_health / 10))
    print('------------------------------------------')
    if player2.health <= 0:
        os.system("cls")
        print(player1.name + "승리!")
        print('승자의 남은 체력 : %.2f ' % (player1.health / 10))
        print('최후의 일격 : %s, %d 데미지' % (attack[1], attack[2]))
        print('진행한 턴 수 : %d' % turn)
        break
    attack = player2.attack(player1)
    print('%s의 공격\n %s %d 데미지\n %s의 남은 체력 : %d / %d' % (attack[0],
                                                        attack[1],
                                                        attack[2],
                                                        attack[3],
                                                        attack[4],
                                                        player1.original_health / 10))
    print('------------------------------------------')
    if player1.health <= 0:
        os.system("cls")
        print(player2.name + "승리!")
        print('승자의 남은 체력 : %.2f ' % (player2.health / 10))
        print('최후의 일격 : %s, %d 데미지' % (attack[1], attack[2]))
        print('진행한 턴 수 : %d' % turn)
        break
    time.sleep(0.5)
    turn = turn + 1
