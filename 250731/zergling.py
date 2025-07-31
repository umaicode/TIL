class ZergLing:
    # 생성자
    def __init__(self):
        self.hp = 20  # 인스턴스 변수, 속성, 필드
        self.mana = 50

    # 메서드
    def run(self):
        print("뛴다")
        self.hp -= 1
        self.mana += 1

    # 메서드
    def show_status(self):
        print(f"현재 HP : {self.hp}, 현재 MP : {self.mana}")


z1 = ZergLing()
z2 = ZergLing()
z1.run()  # 한번 뛰고
z1.show_status()  # 상태 출력
for _ in range(5):
    z2.run()
z2.show_status()
