# https://leetcode.com/problems/text-justification/
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        one_line = []
        line_count = 0
        for word in words:
            new_len = len(word) if line_count is 0 else line_count + 1 + len(word)
            # 如果加上新单词会超过maxWidth，则对这一行进行处理
            if new_len > maxWidth:
                space_num = maxWidth - line_count
                # 只有一个单词的场合，直接在其后面用空格填满
                if len(one_line) is 1:
                    one_line[0] += " " * space_num
                # 有多个单词的场合，对于除了最后一个单词的单词，一个个在其后面添加空格
                # 从左到右遍历，之后又回到左，依次添加空格，满足题目要求的尽量平均、左边优先
                else:
                    index = 0
                    while space_num:
                        one_line[index] += " "
                        space_num -= 1
                        index = (index + 1) % (len(one_line) - 1)
                result.append("".join(one_line))
                one_line = [word]
                line_count = len(word)
            else:
                # 加上新单词不超过maxWidth，则加上新单词
                if one_line:
                    one_line[-1] += " "
                    line_count += 1
                one_line.append(word)
                line_count += len(word)

        result.append("".join(one_line) + " " * (maxWidth - line_count))
        return result


s = Solution()
print(s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 14))
