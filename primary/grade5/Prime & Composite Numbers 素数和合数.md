# Prime Numbers and Factors 素数和因数（质数和约数）

## Factors 因数

"**Factors 因数**" are the numbers you multiply together to get another number:

$\because$ factors $1 \times 6=2\times3=6, \therefore$ 6的因数有 $1,2,3,6$

## Factor Tree 因数树，树枝分解法

a "**Factor Tree 因数树**" can help: find any factors of the number, then the factors of those numbers, etc, until we can't factor any more.

## 素数和合数的定义

A **Prime Number 素数** is:

    a whole number greater than 1 that can not be made by multiplying other whole numbers

The first few prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19 and 23, and we have a prime number chart if you need more.  

(1) 只能被 **1和自己** 整除的自然数，称为素数，也叫质数，否则就是合数。或    
(2) 只有 **1和自己** 这两个正因数的自然数称为素数；比1大且不是素数的自然数就是合数。 

If we can make it by multiplying other whole numbers it is a **Composite Number 合数**, such as 4=2 $\times$ 2.

## Prime Factorization 素因数分解（分解质因数）

"**Prime Factorization 素因数分解**" is finding which prime numbers multiply together to make the original number.

**分解素因数**：一个合数用几个素数相乘的形式表示出来，叫做分解素因数，其中每个素数都是这个合数的素因数。

## GeoGebra中作程序实现

- 添加乘号文本：text1=\times
- 添加输入合数框：
- 对合数框进行因数分解：M_1 = Factors(n)
- L_1=Zip(power(Element(p, 1), Element(p, 2)), p, M_1)
- L_2=Append(L_1(1), Sequence(text1 + (L_1(i)), i, 2, Length(L_1)))

## 哥德巴赫猜想 Goldbach Conjecture

任何大于2的偶数都可以分解为两个素数之和，这是欧拉的表述，被人称为“**关于偶数的哥德巴赫猜想**”或“**强哥德巴赫猜想**”。

“任一大于7的奇数都可写成三个质数之和的猜想”，这被称为“**弱哥德巴赫猜想**”或“**关于奇数的哥德巴赫猜想**”。

1966年，陈景润证明了"1+2"成立，即"任一充分大的偶数都可以表示成二个素数的和，或是一个素数和一个**半素数**的和"。

数学中，两个素数的乘积所得的自然数我们称之为**半素数**（也叫双素数，二次殆素数）开始的47个半素数是4,6,9,10,14,15,21,22,25,26,33,34,35,38,39,46,49,51,55,57,58,62,65,69,74,77,82,85,86,87,91,93,94,95,106,111,115,118,119,121,122,123,129,133,134,141,142... 它们包含1及自己在内合共有3或4个因子。

## 偶数合数的分解

1. 合数可以分解为素因数的乘积
2. 大于2的偶数可以分解为两个素数的和
3. 大于7的奇数可以分解为三个素数之和

**举例**     
- 分解素因数：$147 = 3 \times 49= 3\times 7\times 7 = 3\times 7^2$
- 素数之和：$147=139+3+5=137+3+7=131+5+11+\cdots$
- 分解素因数：$90 = 9 \times 10 = 3^2 \times 2\times 5=2\times 3^2 \times 5$
- 素数之和：$90=7+83=11+79=17+73=19+71=23+67=29+61=31+59=37+53=43+47$

## 利用短除法求素因数

$最小素因数p_1|\underline{待分解的整数}$  
$\quad最小素因数p_2|\underline{商}$  
$\qquad最小素因数p_3|\underline{商}$  
$\qquad \quad最小素因数p_4|\underline{商}$  
$\qquad \qquad 最小素因数p_5|\underline{商}$  
$\qquad \qquad \qquad\cdots\cdots\cdots|\underline{商}$  
$\qquad \qquad \qquad最小素因数|\underline{1}$  

## Why find Prime Factors? 为何要素因数分解

A prime number can only be divided by 1 or itself, so it cannot be factored any further!

Every other whole number can be broken down into prime number factors.

It is like the Prime Numbers are the basic building blocks of all numbers.

This idea can be very useful when working with big numbers, such as in **Cryptography 密码学**.

And here is another thing:

**`There is only one (unique!) set of prime factors for any number.`**

## 素数的特性

1. 质数 $p$ 的约数只有两个：$1$ 和 $p$；
2. 大于2的素数只能是奇数；
3. 0和1既不是素数也不是合数；
4. 2是唯一的偶素数；
5. 初等数学基本定理：任何大于1的自然数，要么本身是质数，要么可以分解为几个质数之积，且这种分解是唯一的；
6. 质数的个数是无限的；
7. 质数的个数公式 π(n) 是不减函数；
8. 若n为正整数，在 $n^2$ 到 $(n＋1)^2$ 之间至少有一个质数；
9. 若质数 $p$ 为不超过 $n(n≥4)$ 的最大质数，则 $p\gt\frac{n}{2}$；
10. 所有大于 $10$ 的质数中，个位数只有 $1,3,7,9$。

证明：质数的个数是无穷的。

欧几里得的《几何原本》中的证明使用了反证法。  
具体证明如下：假设质数只有有限的 $n$ 个，从小到大依次排列为 $p_1，p_2，\cdots，p_n$，设 $N=p_1×p_2×\cdots×p_n$，那么，$N+1$ 是素数或者不是素数。

1. 如果 $N+1$ 为素数，则 $N+1$ 要大于 $p_1，p_2，\cdots，p_n$，所以它不在那些假设的素数集合中。
2. 如果 $N+1$ 为合数，因为任何一个合数都可以分解为几个素数的积；而 $N$ 和 $N+1$ 的最大公约数是1，所以 $N+1$ 不可能被 $p_1，p_2，\cdots，p_n$ 整除，所以该合数分解得到的素因数肯定不在假设的素数集合中。

## Prime number chart 素数表(<100)

$\large \textcolor{red}{100以内的素数表(共25个素数，占比25\%)}$

|范围|个位1|个位3|个位7|个位9|素数个数|
|---|---|---|---|---|---|
|(1,10)|2|3|5|7|4|
|(10,20)|11|13|17|19|4|
|(20,30)||23||29|2|
|(30,40)|31||37||2|
|(40,50)|41|43|47||3|
|(50,60)||53||59|2|
|(60,70)|61||67||2|
|(70,80)|71|73||79|3|
|(80,90)||83||89|2|
|(90,100)|||97||1|

注意：除第一行外，其它行都是对应末尾位。

$\Large Prime\; Numbers\; below\; 100\\ \textcolor{red}{——小于100的素数表——}\\[1em]
 \;\;2 \;\;3\;\; 5\;\; 7\; \\
 11\; 13\; 17\; 19\;\\ 
 23\; 29\; \\
 31\; 37\;\\
 41\; 43\; 47\;\\ 
 53\; 59\;\\ 
 61\; 67\;\\ 
 71\; 73\; 79\\ 
 83\; 89\\ 
 97$

## Prime number chart 素数表(<1000)

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]