"""
https://paiza.jp/botchi/challenges/botchi_c_3002

PAIZA病院のシステムを解析します。
不正アクセスを試みるクラッカーからユーザーを守るために、ユーザーが設定するパスワードが十分に複雑であるようにしなくてはなりません。
PAIZA病院は、パスワードの複雑さの条件として以下の 3 つを定めました。

・
・英字と数字の両方を含む必要がある
・同じ文字を 3 つ以上連続で使用することはできない

なお、英字の大文字と小文字は区別する必要はありません。
パスワードの候補が入力として与えられるので、複雑さの条件をすべて満たす場合は "Valid"、そうでない場合は "Invalid" と出力してください。

例えば、入力例 1 で与えられる 7Caaad9 は 1 つ目の条件と 2 つ目の条件を満たしますが、aaa と 3 つ以上同じ文字が連続で使用されているため、複雑さの条件をすべて満たしません。

入力される値
t
・パスワードの候補となる文字列 t が与えられます。
・入力は 1 行となり、末尾に改行が 1 つ入ります。

条件
・1 ≦ (t の長さ) ≦ 30
・文字列 t は半角英字あるいは半角数字で構成された文字列

期待する出力
パスワードが複雑さの要件をすべて満たす場合は "Valid"、そうでない場合は "Invalid" と出力してください。

入力例1
入力
7Caaad9

出力
Invalid

入力例2
入力
DjZGrduN8Mj4

出力
Valid
"""


# 应该是用正则表达式拼配做了四次，然后超时....
# import re
# password = input()
# print("Valid" if re.match("^(?!.{3})(?=.*\d)(?=.*[a-z]).{6,}$", password, re.I) else "Invalid")

def is_valid(password):
    if len(password) < 6:
        return False
    else:
        repeat = 0
        number_exists = False
        alphabet_exists = False
        for i in range(len(password)):
            if i is 0 or password[i] is not password[i - 1]:
                repeat = 1
            else:
                repeat += 1
                if repeat >= 3:
                    return False
            if ord('0') <= ord(password[i]) <= ord('9'):
                number_exists = True
            elif ord('a') <= ord(password[i]) <= ord('z'):
                alphabet_exists = True
        return number_exists and alphabet_exists


password = input().lower()
print("Valid" if is_valid(password) else "Invalid")
