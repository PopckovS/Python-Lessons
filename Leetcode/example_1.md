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


