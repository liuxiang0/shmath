# 约数的个数

为了得到一个数的约数个数，首先需要将这个数进行素因数分解，并将结果写成 **指数形式**，即将相同素因数的乘积写成指数形式。

## 约数个数定理 

一个合数的约数个数，等于它的素因数分解式中每个素因数的个数（即指数）加1的连乘的积。

对于一个大于 1 正整数 $N$ 可以分解质因数：

$N=\prod_{i=1}^{k} p_i^{a_i} = p_1^{a_1}\cdot p_2^{a_2} \cdots p_k^{a_k}$ 

则 $N$ 的正约数的个数就是 $f(N)=\prod_{i=1}^k (a_i+1)=(a_1+1)(a_2+1)\cdots (a_k+1)$  。

其中 $a_1、a_2、a_3、\cdots、a_k$ 是 $p_1、p_2、p_3、\cdots、p_k$的指数

## 分解素因数是关键

Python语言中有一个模块 sympy, 其中有一个函数 factorint(n) 就可以分解素因数。

~~~python
>>> import sympy 
>>> sympy.factorint(32)
{2: 5}
>>> sympy.factorint(132)
{2: 2, 3: 1, 11: 1}
>>> sympy.factorint(35)
{5: 1, 7: 1}
>>> sympy.factorint(360)
{2: 3, 3: 2, 5: 1}
>>> sympy.factorint(240)
{2: 4, 3: 1, 5: 1}
~~~

[GeoGebra](https://ggb123.cn/u/kumath) 中，也有函数 Factors(Number) 进行分解素因数，如 $Factors(32)\to (2 5)$;

同时还可以进行 因式分解 Factors(Polynomial) 可以分解因式，如 $Factors(x^3-1)\to \{\{x-1,1\},\{x^2+x+1,1\}\}$

# 例题1  求32的约数个数和各个约数

解：  
$\qquad \because 32=2^5 \\ \qquad\therefore 32有 (5+1)=6$个约数。

它们分别是 $1\times32,\;2\times16,\;4\times8$

# 例题2  求35的约数个数和各个约数

解：  
$\qquad \because 35=5\times7 \\ \qquad\therefore 35有 (1+1)\times(1+1)=4$个约数。

它们分别是 $1\times35,\;5\times7$

# 例题3  求360的约数个数

解：  
$\qquad \because 360=2^3\times 3^2 \times 5  \\ \qquad\therefore 360有 (3+1)\times(2+1)\times(1+1)=24$个约数。

# 例题4  求240的约数个数

解：  
$\qquad \because 240=2^4\times3\times5,\\ \qquad \therefore 240有(4+1)\times(1+1)\times(1+1)=20$个约数

