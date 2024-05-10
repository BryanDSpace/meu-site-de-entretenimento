import random, pyttsx3, os, time
engine = pyttsx3.init()

lista_Jp = {"A": "HIRAGANA: あ ou KATAKANA: ア", "I": "HIRAGANA: い ou KATAKANA: イ", "U": "HIRAGANA: う ou KATAKANA: ウ", "E": "HIRAGANA: え ou KATAKANA: エ", "O": "HIRAGANA: お ou KATAKANA: オ",
            "KA": "HIRAGANA: か ou KATAKANA: カ", "KI": "HIRAGANA: き ou KATAKANA: キ", "KU": "HIRAGANA: く ou KATAKANA: ク", "KE": "HIRAGANA: け  ou KATAKANA: ケ", "KO": "HIRAGANA: こ ou KATAKANA: コ",
            "SA": "HIRAGANA: さ ou KATAKANA: サ", "SHI": "HIRAGANA: し ou KATAKANA: シ", "SU": "HIRAGANA: す ou KATAKANA: ス", "SE": "HIRAGANA: せ ou KATAKANA: セ", "SO": "HIRAGANA: そ ou KATAKANA: ソ", 
            "TA": "HIRAGANA: た ou KATAKANA: タ", "CHI": "HIRAGANA: ち ou KATAKANA: チ", "TSU": "HIRAGANA: つ ou KATAKANA: ツ", "TE": "HIRAGANA: て ou KATAKANA: テ", "TO": "HIRAGANA: と  ou KATAKANA: ト",
            "NA": "HIRAGANA: な ou KATAKANA: ナ", "NI": "HIRAGANA: に ou KATAKANA: ニ", "NU": "HIRAGANA: ぬ ou KATAKANA: ヌ", "NE": "HIRAGANA: ね ou KATAKANA: ネ", "NO": "HIRAGANA: の ou KATAKANA: ノ",
            "HA": "HIRAGANA: は ou KATAKANA: ハ", "HI": "HIRAGANA: ひ ou KATAKANA: ヒ", "FU": "HIRAGANA: ふ ou KATAKANA: フ", "HE": "HIRAGANA: へ ou KATAKANA: ヘ", "HO": "HIRAGANA: ほ  ou KATAKANA: ホ",
            "MA": "HIRAGANA: ま ou KATAKANA: マ", "MI": "HIRAGANA: み ou KATAKANA: ミ", "MU": "HIRAGANA: む ou KATAKANA: ム", "ME": "HIRAGANA: め  ou KATAKANA: メ", "MO": "HIRAGANA: も  ou KATAKANA: モ",
            "YA": "HIRAGANA: や ou KATAKANA: ヤ", "-": "HIRAGANA: - ou KATAKANA: -", "YU": "HIRAGANA: ゆ ou KATAKANA: ユ", "-": "HIRAGANA:  - ou KATAKANA: -", "YO": "HIRAGANA: よ ou KATAKANA: ヨ",
            "RA": "HIRAGANA: ら ou KATAKANA: ラ", "RI": "HIRAGANA: り ou KATAKANA: リ", "RU": "HIRAGANA: る  ou KATAKANA: ル", "RE": "HIRAGANA: れ ou KATAKANA: レ", "RO": "HIRAGANA: ろ ou KATAKANA: ロ",
            "WA": "HIRAGANA: は ou KATAKANA: ハ", "-": "HIRAGANA: - ou KATAKANA: -", "N": "HIRAGANA: ん  ou KATAKANA: ン", "-": "HIRAGANA: - ou KATAKANA: -", "WO": "HIRAGANA: を ou KATAKANA: ヲ",
            }
romaji = ['A', 'I', 'U', 'E', 'O', 'KA', 'KI', 'KU', 'KE', 'KO', 'SA', 'SHI', 'SU', 'SE', 'SO', 'TA', 'CHI', 'TSU', 'TE', 'TO', 'NA', 'NI', 'NU', 'NE', 'NO', 'HA', 'HI', 'FU', 'HE', 'HO', 'MA', 'MI', 'MU', 'ME', 'MO', 'YA', '-', 'YU', 'YO', 'RA', 'RI', 'RU', 'RE', 'RO', 'WA', '-', 'N', '-', 'WO']
introd = "Instruções\nDigite [dicas] ou [d] no type in romaji: para ter dicas, o custo de uma dica é 2 pontos\nexemplo:\nType in romaji: dicas\nou\nType in romaji: d\nE caso, você erre, você perde um ponto se os pontos chegar em zero é game over"
#print(len(romaji))        #len romaji 49 + 1

game_over = "Version 0.01: in japanese\nGame Over\n\nOlá eu sou um jogo de treinamento em japonês hiragana e katakana, criado Por Bryan, fui feito na linguagem de programação Python.\nTenha bons aprendizados, desejo tudo de bom na sua vida, Jesus te ama!"
ponts = 1
n = 1

while True:
    print("Ouça o áudio")  
    engine.say(introd)
    engine.runAndWait()
    for cont_caracter in range(len(introd)+1):
        print(introd[:cont_caracter])
        time.sleep(0.05)
        os.system("cls")
    print(introd)
    time.sleep(3)
    os.system("cls")
    for i in range(49): 
        
        i_random = random.randint(0, len(lista_Jp))
        print(f"Points {ponts}\n{n}: {lista_Jp[romaji[i_random]]}")
        valor = input("Type in romaji: ").upper().strip()
        if romaji[i_random] == valor:
            print("Você acertou")
            engine.say("Você acertou")
            engine.runAndWait()
            
            ponts = ponts + 1
            
        elif valor == "DICAS" or valor == "D": 
            if ponts >= 2:
                print(print(romaji[i_random]))
                time.sleep(3)
                os.system("cls")
                ponts = ponts - 2
               
        else:
            if ponts == 0:
                for x in range(len(game_over)):
                    print(game_over[:x])
                    time.sleep(0.01)
                    os.system("cls")
                    
                print(f"{game_over}")
                time.sleep(10)
                break
            else:  
                print("Você não acertou, perdeu um ponto")
                engine.say("Você não acertou, perdeu um ponto")
                engine.runAndWait()
                ponts = ponts - 1

        time.sleep(2)
        os.system("cls")
        n = n + 1
        print("Version 0.01: in japanese")
    break