import random


CHOICES = {
    "t": "tosh",
    "q": "qaychi",
    "g": "qog'oz",
}


def decide_winner(user: str, comp: str) -> str:
    if user == comp:
        return "durrang"
    wins = {"tosh": "qaychi", "qaychi": "qog'oz", "qog'oz": "tosh"}
    return "yutdingiz" if wins[user] == comp else "yutqazdingiz"


def prompt_choice() -> str:
    while True:
        ch = input("Tanlov (t=tosh, q=qaychi, g=qog'oz, qutish uchun 'x'): ").strip().lower()
        if ch in {"x", "exit", "q"}:
            raise KeyboardInterrupt
        if ch in CHOICES:
            return CHOICES[ch]
        if ch in CHOICES.values():
            return ch
        print("Noto'g'ri kirish. Qayta urinib ko'ring.")


def game_loop() -> None:
    user_score = 0
    comp_score = 0
    rounds = 0
    print("Tosh-Qaychi-Qog'oz o'yini. Chiqish: x")
    while True:
        try:
            user = prompt_choice()
        except KeyboardInterrupt:
            print("\nChiqildi.")
            break
        comp = random.choice(list(CHOICES.values()))
        result = decide_winner(user, comp)
        rounds += 1
        if result == "yutdingiz":
            user_score += 1
        elif result == "yutqazdingiz":
            comp_score += 1
        print(f"Siz: {user} | Kompyuter: {comp} -> {result}")
        print(f"Hisob: Siz {user_score} : {comp_score} Kompyuter (raundlar: {rounds})\n")


if __name__ == "__main__":
    game_loop()




















