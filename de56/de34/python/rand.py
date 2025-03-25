
#苗字とただしい読み方リスト
kanji_to_yomi={
"剛力":"ごうりき",
"大王":"だいおう",
"凸守":"でこもり",
"神来社":"からいと",
"大豆生田":"おおまめうだ",
"九":"いちじく",
"月見里":"やまなし",
"勘解由小路":"かでのこうじ",
"怒鳴門":"どなるど",
"五百旗頭":"いおべき",}

#リストの作成
kanji_to_yomi= list(kanji_to_yomi.keys())

#出題の初期化コマンド

question_index = 0


#ゲームのループ

while question_index < len(kanji_list):
 kanji = kanji_list[question_index]
 correct_yomi = kanji_to_yomi[kanji]
 user_input = input(f"この人あったことある...苗字は確か...{kanji}")
                    
if user_input == correct_yomi:
  print("あ、危ねぇ！覚えてた...。よかった...。")   

else:
   print (f"違った.....。気まずい....。もしかして「{correct_yomi}」だった気がする。")

   #次の問題
   question_index += 1

   print("苗字難しすぎだろ！！！")
