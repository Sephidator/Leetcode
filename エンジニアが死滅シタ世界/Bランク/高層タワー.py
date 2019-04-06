"""
https://paiza.jp/botchi/challenges/botchi_b_2001

単語を組み合わせて新単語を作ります。
新単語は N 個の文字列を、前から順に結合して作ります。

この時、冗長さをなくすため、 前から結合した単語の末尾 と 後ろの単語の先端 が一番長く一致するように結合します。

例えば、 入力例 1 の "paiza", "apple", "letter" の場合、
先頭から "paiza", "apple" を条件どおり重ねると "paizapple" となります。
この単語を更に次の単語と重ねると "paizappletter" となります。



なお、必ず前から順番に重ねるため、 入力例 2 の "poh", "p", "oh" を結合する場合は、
"poh" と "p" を重ねた後の単語 "pohp" と "oh" を重ね "pohpoh" となります。

N 個の単語が与えられるので、前から順番に単語を結合した場合の新単語を出力してください。

入力される値
N
w_1
w_2
...
w_N
・1 行目に、結合する単語の数を表す整数 N が与えられます。
・続く N 行のうちの i 行目 (1 ≦ i ≦ N) には、 i 番目に結合する単語を表す文字列 w_i が与えられます。
・入力は合計 N + 1 行であり、最終行の末尾に改行が 1 つ入ります。

条件
・2 ≦ N ≦ 100
・各 i (1 ≦ i ≦ N) に対して以下を満たす。
　・1 ≦ (w_i の長さ) ≦ 100
　・w_i は半角英小文字のみで構成されている。

期待する出力
N 個の単語を前から順番に、条件どおりに結合した際の新単語を出力してください。

入力例1
入力
3
paiza
apple
letter

出力
paizappletter

入力例2
入力
3
poh
p
oh

出力
pohpoh
"""

N = int(input())
result = ""

for _ in range(N):
    string = input()
    match_len = len(string)
    # 注意这里不能用is not，is是值判断+引用判断，!=是单纯比较值
    while result[len(result) - match_len:] != string[0:match_len]:
        match_len -= 1
    result += string[match_len:]

print(result)
