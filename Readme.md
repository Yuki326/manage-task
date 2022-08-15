// 2022-8.txt
ブランチ　説明　時間　状態
A-10 # 5h low // wait,done,high,medium
A-13 機能実装 3h2m done

sh record.sh AT-10 +3h10m // -も可
#=> A-10 # 8h10m

cat taskRecord/2022-8.txt
#=>
A-10 バグ修正 8h10m medium
A-13 機能実装 3h2m done

#discordbot=> +3h10m AT-10//時間でソートする処理も行う

sh record.sh A-10 $バグ修正 //組み合わせ可

sh record.sh A-10 ->medium

sh taskRecord/getSumTime.sh 2022-8 　// 省略した場合今月
#=> sum:11h12m

toExcel.sh 2022-8.txt

// 日付ごとでも取得したい
2022-8Date.txt
1 A-10:3h10m A-8:2h5m
2
