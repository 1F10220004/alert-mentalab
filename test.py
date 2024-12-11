

def janken_game():
    print("じゃんけんゲームを始めましょう！")
    print("選択肢: 0: グー, 1: チョキ, 2: パー")
    
    options = ["グー", "チョキ", "パー"]
    
    # プレイヤーの選択
    player_choice = int(input("あなたの選択は？ (0, 1, 2): "))
    if player_choice < 0 or player_choice > 2:
        print("無効な選択です。0, 1, 2 のいずれかを選んでください。")
        return
    
    # コンピュータの選択
    computer_choice = random.randint(0, 2)
    
    print(f"あなたの選択: {options[player_choice]}")
    print(f"コンピュータの選択: {options[computer_choice]}")
    
    # 結果判定
    if player_choice == computer_choice:
        print("結果: 引き分けです！")
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 0):
        print("結果: あなたの勝ちです！")
    else:
        print("結果: あなたの負けです！")

# ゲームを実行
janken_game()
