## kmp算法
比较好的文章：http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

## 要点
主字符串s，要判断的字符串t

* 通过s不回退的方式保证已经知道不相等的不用再判断了
* 通过t的不固定的回退方式来保证已经判断过相等的就不用再判断了
