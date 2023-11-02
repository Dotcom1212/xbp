age=18+10
age=20-age
age=age*2
age=age/3



for i in range(3):

        #文字だからダブルクオーテーションを入れる
    print(i,"人目")
    name=input("あなたの名前を入れてください")
    waist=float(input("あなたの腹囲の数値を教えてください"))
    age=int(input("あなたの年齢を教えてください"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    #ここからが条件分岐
    if waist>=85 and age>=40:#この部分が変更されました
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さんの腹囲は問題ありません。けどもっと食え！")


