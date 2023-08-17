1) Two-sum

Используя массив целых чисел `nums` и целое число `target`, верните
индексы двух чисел так, чтобы они в сумме составляли `target`

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for k, v in enumerate(nums):
            # Вычитая из target число первого элемента мы оставляем такую часть
            # от target что если такого же значения нет в массиве nums то и решения нет
            res = target - v 
            if res in nums[k+1:]:
                return [k, nums[k+1:].index(res) + k + 1]
```

---

14) Longest Common Prefix

Напишите функцию, которая находит самую длинную строку общего префикса среди массива строк.
Если общего префикса нет, вернуть пустую строку "".


```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ''
        for k in range(0, len(min(strs))):
            res = {word[k] for word in strs}
            if len(res) == 1:
                pre += next(iter(res))
                continue
            break
        return pre
```

---

20) Valid Parentheses

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mix = {"{": "}", "(": ")", "[": "]"}
        stack = []
        
        # check on valis input 
        if not (s and
                len(s) % 2 == 0 and
                s[0] in mix.keys() and
                set(s).issubset(set(list(mix.keys()) + list(mix.values())))):
            return False

        # we fill the stack with symbols and remove the opposite ones from it
        for elem in s:
            if elem in mix.keys():
                stack.append(elem)
            else:
                if len(stack) > 0 and mix[stack[-1]] == elem:
                    stack.pop()
                else:
                    return False
                
        # if there is anything left
        if len(stack) > 0:
            return False

        return True
```

test-case

```python
    params = {
        "(){}}{": False, 
        "()": True, 
        "()[]{}": False, 
        "(]": False, 
        "{[]}": True, 
        "": False, 
        "{": False, 
        ")": False,
        "{([[({([])})]])}": True, 
        "{([[({([(])})]])}": False, 
        "{([[({([])})]])}}": False
    }
    s = Solution()
    for case, answer in params.items():
        print(f"Input: {case}  Expected: {answer} Output: {s.isValid(case)}")
        print('='*40)
```

---

58) Length of Last Word

Учитывая строку s, состоящую из слов и пробелов, вернуть длину последнего слова в строке.

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])
```

---

66) Plus One

Вам дано большое целое число, представленное в виде массива целых чисел `digits`,
где каждое число `digits[i]` является цифрой целого числа. Цифры упорядочены от наиболее
значащего к наименее значащему в порядке слева направо. Большое целое число не содержит
начальных символов равных 0

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, str(int(''.join(map(str, digits)))+1)))
```


