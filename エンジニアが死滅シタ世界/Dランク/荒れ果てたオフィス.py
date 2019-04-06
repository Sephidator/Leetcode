"""
https://paiza.jp/botchi/challenges/botchi_d_4002

あなたは書類の整理をしています。
書類には 1 から 3 までの重要度 e が設定されています。数字が大きいほど重要な書類とされています。

書類のタイトル文字列 S_i と重要度 e_i が n 件与えられます。
重要度が 3 の書類のタイトルのみを入力された順に出力してください。

入力される値
n
S_1 e_1
...
S_n e_n
・1 行目は与えられる書類の件数 n が与えられます。
・2 行目から 2 + n 行目に書類のタイトル文字列 S_i と重要度 e_i が与えられます。
・入力は 2 + n 行となり、末尾に改行が 1 つ入ります。

条件
・1 ≦ n ≦ 100
・1 ≦ 文字列 S_i の長さ ≦ 100
・S_i は半角アルファベットで構成された文字列
・e_i は 1, 2, 3 のいずれかの整数
・必ず e_i が 3 の書類は 1 件以上存在する

期待する出力
重要度が 3 の書類のタイトルのみを入力された順に出力してください。


入力例1
入力
5
paiza 1
coding 3
answer 3
input 2
aaaaa 1

出力
coding
answer

入力例2
入力
1
Paiza 3

出力
Paiza
"""


n = int(input())
for _ in range(n):
    record = input().split()
    if int(record[1]) is 3:
        print(record[0])
