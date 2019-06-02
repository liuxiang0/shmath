# Math 2019 Shanghai Gaokao 上海2019高考数学复习

## 圆锥曲线--Conic Curve复习

### 概述

标准圆锥曲线的标准方程表示需要熟练掌握，熟练圆锥曲线的几何意义，并能通过几何描述语言，运用代数方法，轻松写出曲线方程。

本节包括以下几部分：
1. 抛物线Parabola
2. 双曲线Hyperbola
3. 椭圆Ellipse
4. 圆Circle
5. 曲线和方程
6. 综合题

用一个平面去截一个锥体，得到不同圆锥曲线。
![image](images/conic_sections.png)

圆锥曲线的一般方程为：
$$ax^2+bxy+cy^2+dx+ey+f=0$$

### 抛物线Parabola

图形|标准方程|焦点坐标|准线方程|其它内容
---|----|----|----|---
![image](images\parabola_1.png)|$y^2=2px (p>0)$|($\frac{p}{2}$,0)|$x=-\frac{p}{2}$|
![image](images\parabola_2.png)|$y^2=-2px (p>0)$|(-$\frac{p}{2}$,0)|$x=\frac{p}{2}$|
![image](images\parabola_3.png)|$x^2=2py (p>0)$|(0,$\frac{p}{2}$)|$y=-\frac{p}{2}$|
![image](images\parabola_4.png)|$x^2=-2py (p>0)$|(0,-$\frac{p}{2}$)|$y=\frac{p}{2}$|

* 注意：初中阶段，解过一元二次方程$ax^2+bx+c=0$,实际上就是从函数$f(x)=ax^2+bx+c$到抛物线图形与x轴的交点的转换，也可以理解为一元二次多项式$ax^2+bx+c$的因式分解问题。
* 任何形如$y=ax^2+bx+c$都可以通过坐标变换，转换成上述表格中的标准方程。如$y=a(x-h)^2+k$,定点是$(h，k)$，或者 $y=a(x-x_1)(x-x_2)$,与x轴有两个交点$(x_1,0),(x_2,0)$.
* 韦达定理： $x_1+x_2=-\frac{b}{a}， x_1 \cdot x_2=\frac{c}{a}$
* 对称轴为$x_k = -\frac{b}{2a}$


#### 几何意义

平面中，到一个定点与到一条定直线的距离相等的图形就是抛物线。其中定点就是焦点$F$，定直线就是准线$l$。

![image](images/parabola(2).png)


#### 物理意义

在抛物线焦点放置一个点光源，通过抛物面反射后成为平行线折射出去。

![image](images/parabola(2).jpg)
![image](images/parabolic_reflector(2).jpg)
![image](images/78431210(2).jpg)

#### 举例

J1P1T5 （4分）

若点F为抛物线$y=2x^2$的焦点，点P为抛物线上的任意一点，则PF的中点M所满足的方程为__________________

J2P7T8 (5分)

已知抛物线C：$y^2=2px(p>0)$的焦点为F, 点M在C上，|MF|=10,若以MF为直径的圆过点（0，4），则C的方程是_______________________________


### 双曲线 Hyperbola

图形|标准方程|焦点坐标|顶点|准线方程|渐近线
---|----|----|----|---|---
![image](images\hyperbola_1.png)|$\frac{x^2}{a^2} - \frac{y^2}{b^2}=1(a>0,b>0)$|($\pm c$,0),($c^2=a^2+b^2$)|($\pm a$,0)|$x=\pm\frac{a^2}{c}$|$\frac{x}{a}\pm\frac{y}{b}=0$
![image](images\hyperbola_2.png)|$\frac{y^2}{a^2} - \frac{x^2}{b^2}=1(a>0,b>0)$|(0,$\pm c$),($c^2=a^2+b^2$)|(0,$\pm a$)|$y=\pm\frac{a^2}{c}$|$\frac{y}{a}\pm\frac{x}{b}=0$

#### 几何意义

平面中，到两个定点的距离之差的绝对值等于常数$2a$的点的轨迹就是双曲线。其中定点就是焦点$F_1, F_2$，$a$是双曲线的实半轴, $b$是双曲线的虚半轴。

离心率$e=\frac{c}{a}, \because c^2=a^2+b^2>a^2, \therefore e>1$

如果考虑复数，双曲线可以看成虚椭圆。
$\frac{x^2}{a^2}+\frac{y^2}{(ib)^2}=1$

#### 参数方程

标准方程|参数方程|参数
----|-----|-----
$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$|$x=a\sec\theta, y=b\tan\theta$|$a>0,b>0$
$\frac{y^2}{a^2}-\frac{x^2}{b^2}=1$|$y=a\sec\theta, x=b\tan\theta$|$a>0,b>0$

#### 举例

J2P7T6 （4分）

双曲线$\frac{x^2}{3}-y^2=1$的左右焦点分别为$F_1,F_2$, 过右焦点$F_2$的直线与双曲线的右分支相交于P、Q两点，且点P的横坐标为2，则$\triangle PF_1Q$的周长为__________.



### 椭圆 Ellipse

图形|标准方程|焦点坐标|顶点|准线方程|其它
---|----|----|----|---|---
![image](images\ellipse_1.png)|$\frac{x^2}{a^2} + \frac{y^2}{b^2}=1(a>b>0)$|($\pm c$,0),($c^2=a^2-b^2$)|($\pm a$,0),(0,$\pm b$)|$x=\pm\frac{a^2}{c}$|
![image](images\ellipse_2.png)|$\frac{y^2}{a^2} + \frac{x^2}{b^2}=1(a>b>0)$|(0,$\pm c$),($c^2=a^2-b^2$)|($\pm b$,0),(0,$\pm a$)|$y=\pm\frac{a^2}{c}$|

#### 几何意义

平面中，到两个定点的距离之和等于常数$2a$的点的轨迹就是椭圆。其中定点就是焦点$F_1, F_2$，$a$是椭圆的**长半轴**, $2a$是**长轴长**，$b$是椭圆的**短半轴**，$2b$是**短轴长**。

**离心率** $e=\frac{c}{a}, \because c^2=a^2-b^2<a^2, \therefore 0<e<1$

如果$a=b$，椭圆就退化成圆，圆的焦点就一个，离心率为0。

#### 参数方程

标准方程|参数方程|参数
----|-----|-----
$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$|$x=a\cos\theta, y=b\sin\theta$|$a>b>0$
$\frac{y^2}{a^2}+\frac{x^2}{b^2}=1$|$y=a\cos\theta, x=b\sin\theta$|$a>b>0$


#### 举例


**定理：圆锥曲线的斜率之积为定值**
1. 椭圆顶点$A_1(a,0), A_2(-a,0)$,过原点的直线与椭圆交于B、C两点，P为椭圆上任一点，则
$k_{PA_1} \times k_{PA_2}$ 为定值，
$k_{PB} \times k_{PC}$ 也为定值。

同理：圆、双曲线也都有类似的性质。

### 圆Circle

圆就是特殊的椭圆，长半轴=短半轴=半径的椭圆，两个焦点退化成一个焦点就是圆心O。几何含义就是|PO|=r（半径）。写成集合就是{点P| PO距离为定值，称为半径，即|PO|=r>0}，体现在周长上。

圆心为原点(0,0),半径为r的圆的标准方程为： $x^2+y^2=r^2$

圆心为$(x_0,y_0)$,半径为r的圆的标准方程为：$(x-x_0)^2+(y-y_0)^2=r^2$



**圆饼**的集合就是 { 点P| PO距离不大于定值r，即 |PO| $\le$ r },体现在面积上。

有关$\pi$的几个级数之和有：

$$\frac{\pi}{4}=\frac{1}{1}-\frac{1}{3}+\frac{1}{5}+\cdots=\sum_{i=1}^{\infty}(\frac{1}{4i-3}-\frac{1}{4i-1})$$

$$\frac{\pi^2}{6}=\frac{1}{1^2}+\frac{1}{2^2}+\frac{1}{3^2}+\cdots=\sum_{i=1}^{\infty} \frac{1}{i^2}$$

### 如何用多项式逼近（或表示） $\sin(x)?$

从方程角度出发，我们知道$\sin(x)=0$的解集为$\{0\} \bigcup \{\pm k \pi, k \in N^*\}$.

通过多项式乘积可以预测 

$$a\times x\prod_{i=1}^{\infty} (1 + \frac{x}{k\pi})(1 - \frac{x}{k\pi})$$ 

与 $\sin(x)=0$ 有同样的解。

稍作变化，假定$x$ 不等于 $0$, 则

$$\frac{\sin x}{x}=0$$

与多项式

$$a\times \prod_{i=1}^{\infty} (1 + \frac{x}{k\pi})(1 - \frac{x}{k\pi})=0$$

有相同的解，两边对$x$取极限，利用著名的极限

$$\lim_{x\rightarrow 0}\frac{\sin x}{x}=1$$

可以求得$a=1$.

$$\therefore \sin(x)=x\prod_{i=1}^{\infty} (1 + \frac{x}{k\pi}) (1 - \frac{x}{k\pi})$$


### 综合题

J2P9T19 (14分，(1)5分 （2）9分）

定义：在平面内，点P到曲线C上的点距离的最小值称为P到曲线C的距离。

已知：圆M： $(x-\sqrt5)^2+y^2=36$及点N(-$\sqrt5$,0), 动点P到圆M的距离与到点N的距离相等，记点P的轨迹为曲线W。

（1）求曲线W的方程；

（2）若直线$l$与曲线W在$x$轴上、下部分分别交于点P、Q，与$x$轴交于点$T（t,0)（t<0)$, 且$|PT|=2|TQ|$, 求当$\triangle OPQ$的面积取最大值时直线$l$的方程。




J3P16T20 (16分，（1)4分（2）6分（3）6分）

已知椭圆C：$\frac{x^2}{2}+y^2=1$的左焦点为F，O为坐标原点。

![image](images\j3p16t20.png)

（1）设点M为椭圆C上任意一点，求$\overrightarrow {MF} \cdot \overrightarrow {MO}$的最小值；

（2）求过点O、F，并且与直线$l: x=-2$相切的圆的方程；

（3）设过点F且不与坐标轴垂直的直线交椭圆C于点A、B两点，椭圆C上是否存在点P，使得$\overrightarrow{AP}=\overrightarrow{OB}$？若存在，求点P的坐标；若不存在，说明理由。

--------------------------

## 例题解答


* J1P1T5
【解】

首先是化成标准方程，然后从熟悉的标准方程得到焦点坐标，考察抛物线基础知识以及几何基本知识，还有如何根据几何条件，利用代数知识得到轨迹方程。

$\because y = 2 x^2, \therefore x^2 = \frac{1}{2} y, 2p=\frac{1}{2}, p=\frac{1}{4}, c=\frac{p}{2}=\frac{1}{8}, F$ 在y轴正方向上，$\therefore F(0,c)=F(0,\frac{1}{8})$.

设M的坐标为$M(x,y)$, 由题意，M是PF的中点，所以点P的坐标为$P=2M-F=(2x,2y)-F(0,c)=(2x, 2y-c), \because P \in \{(x,y)|y=2x^2\}, \therefore$ 点P满足抛物线方程，即

$$2y-c = 2(2x)^2, y=\frac{c}{2}+4x^2, \therefore y=4x^2+\frac{1}{16}$$

* J2P7T8
  【解】
  
  了解抛物线基本知识焦点，圆的基本知识，以及由此写曲线方程。

  由已知，得到抛物线C的焦点F在x轴正方向上，且$F(\frac{p}{2},0)$, 设$A(0,4)$, 点$M(x,y)$, 由已知可得：

  $$\because M \in C, \therefore y^2=2px$$

  $$\because |MF|=10, \therefore (x-\frac{p}{2})^2+y^2=100$$

  $$\because A \in Circle, \therefore MF \perp MA, k_{MF}\times k_{MA}=-1,\\ \frac{y-4}{x} \dot \frac{0-4}{\frac{p}{2}-0}=-1,\\ px=8(y-4)$$

以上方程组消除$x，y$，求得$p$。
先消除$y$，$y=\sqrt{2px}$

$$(x+\frac{p}{2})^2 = 100$$
$$px=8(\sqrt{2px}-4)$$

由题设显然有 $x \ge 0, p \gt 0$, 故
$x+\frac{p}{2}=10$

$\because (\sqrt{2px}-8)^2 = 0, \therefore 2px = 64$

联立解方程组，不难得到 
$$p(10-\frac{p}{2})=32, \therefore p_1=16, p_2=4$$

经验算，$y^2=8x, y^2=32x$都是C的方程。

* J2P2T6
  【解】
  
  从双曲线基本方程，得到两焦点坐标，直线与双曲线交点与三角形周长，都是基础知识。

  从已知的双曲线方程，可得两焦点在x轴上，且$a^2=3, b^2=1 \therefore c^2=a^2+b^2=4, c=\pm 2$, 两焦点坐标分别为$F_1(-2,0), F_2(2,0)$, 

  已知$P(2,m)$, 则 $\frac{4}{3}-m^2=1$, 由对称性，取$m>0$, 有
  $m=\frac{\sqrt 3}{3}$

  且$PQ \perp F_1F_2, |PQ|=2|PF_2|=\frac{2\sqrt3}{3}$,

  $\because |PF_1| - |PF_2| = 2a, \\\therefore |PF_1| = \frac{\sqrt 3}{3} + 2 \sqrt 3  = \frac{7\sqrt 3}{3}$

  $\triangle PF_1Q$的周长$=2|PF_1|+|PQ|=\frac{14\sqrt3}{3}+\frac{2\sqrt3}{3} = \frac{16 \sqrt 3}{3}$

  注意：为了加快计算，这里没有采用两点之间的距离公式来求$|PF_1|$.

* J2P9T19
  【解】
  
  本题自定义一个数学概念，通过自定义概念出题，是为了考察学生运用数学知识自创题目，并提高数学运用能力。考察圆和动点，几何上的距离的灵活运用。

  设A为圆M上的任意一点，连接圆M的圆心M与A，显然要在MA上找到一点P，满足|PA|=|PN|，或者假定P满足题设，则有P在MA上，且|PA|=|PN|，所以点P满足：
  |PM|+|PN|=|PM|+|PA|=|MA|=6, 满足椭圆性质，$\because 2c=|MN|=2\sqrt5, \therefore c=\sqrt 5;\\ \because 2a=6, \therefore a=3; \\ \because c^2 = a^2 - b^2, \therefore b=2$。
  
  (1) 左右焦点N，M在$x$轴上，且长半轴和短半轴长分别为3和2的椭圆方程为：
    $$\frac{x^2}{9}+\frac{y^2}{4}=1$$
    ![image](images/j2p9T19.png)

  (2) 对于过$x$轴上点$T(t,0)$的直线$PQ$，可以用截距法设该直线方程为：
  $x=my+t (t<0)$, 由题设还知 $-3<t$ 才能交椭圆上下于两点P、Q, 联立方程组得到：
    $$\left \{ \begin{array}{rcl} x=my+t & (1) \\
      \frac{x^2}{9}+\frac{y^2}{4}=1 & (2) 
    \end{array}  \right.$$
    记$P(x_1,y_1), Q(x_2, y_2)$, 由此推出：
    $$4(my+t)^2+9y^2=36 \\
      (4m^2+9)y^2+8mty+(4t^2-36)=0$$
    $$\therefore \left \{ 
        \begin{array}{rcl}
        y_1+y_2 = -\frac{8mt}{4m^2+9} & (3) \\ 
        y1 \cdot y_2 = \frac{4t^2-36}{4m^2+9} & (4) 
        \end{array} 
        \right. $$

    又$\because \overrightarrow{PT} = 2 \overrightarrow{TQ}, \\ \therefore (x_1-t, y_1-0)=2(t-x_2,0-y_2)$

    $$\therefore \left \{  \begin{array}{rcl}
        x_1-t=2t-2x_2 & (5)\\ y_1=-2y_2 & (6)        
    \end{array}  \right.$$

    由（6）代入（3）、（4），得到：
    $$-y_2 = -\frac{8mt}{4m^2+9}, \\ -2y_2^2 = \frac{4t^2-36}{4m^2+9}$$

    $$\therefore 2(\frac{8mt}{4m^2+9})^2=\frac{4t^2-36}{4m^2+9}$$
    解得
    $$m^2 = \frac{9-t^2}{4(t^2-1)}, \\ \because m^2 \ge 0, \therefore 1<t^2<9$$

    从而得到

    $$y_2^2 = \frac{18-2t^2}{4m^2+9} = \frac{2(9-t^2)}{4 \times \frac{9-t^2}{4(t^1-1)}+9}=\frac{(t^2-1)(9-t^2)}{4t^2}$$

    因为$\triangle OPQ$ 的底OT已知，故三角形的面积等于
    $$S_{\triangle {OPQ}} = \frac{1}{2}|t||y_1-y_2|\\
    =\frac{3}{2}|t||y_2|=\frac{3}{2} \sqrt{t^2 y_2^2}\\
    =\frac{3}{4} \sqrt{-(t^2-5)^2+16}$$

    当$t^2=5, t=-\sqrt 5<0$时，上述面积最大，此时，$m^2 = \frac{9-5}{4(5-1)} = \frac{1}{4}, m=\pm \frac{1}{2}$。
    得到直线方程为 $l \colon x=\pm \frac{1}{2} y-\sqrt5$,  $y = \pm 2(x+\sqrt 5)$.

    
    ![image](images/j2p9t19-2.png)
    
特点：求最值的计算量较大，需要一些技巧，时刻关注最终结果，减少不必要的运算。

* J3P16T20
  椭圆综合题，考察最小值问题，直线与圆相切问题，等等

  【解】

(1)设点$M(x_0,y_0)$, 已知椭圆的$a^2=2, b^2 =1$ ,故 $c^2=a^2-b^1=2-1=1
  \therefore c= \pm 1, F(-1,0)$,

  $\overrightarrow{MF} \cdot \overrightarrow{MO}=(\overrightarrow{MO}+\overrightarrow{OF}) \cdot \overrightarrow{MO} =\overrightarrow{MO}^2+\overrightarrow{OF}\cdot\overrightarrow{MO}=x_0^2+y_0^2+x_0=\frac{1}{2}x_0^2+x_0+1, x_0 \in [-\sqrt2,\sqrt2]$

  当$x_0=-1$时，上式取最小值$\frac{1}{2}$。

(2)过点O,F，并与直线x=-2相切的圆，其圆心一定在线段OF的中垂线上，故可设该圆的圆心为 $(-\frac{1}{2},t)$,故圆心到x=-2的距离就是该圆的半径，半径为$r=|-\frac{1}{2}-(-2)|=\frac{3}{2}$.

又$|OF|^2 = r^2, (\frac{1}{2})^2+t^2=\frac{9}{4}$, 解得 $t= \pm \sqrt 2$.

圆的方程有两个：

$(i ) (x+\frac{1}{2})^2+(y-\sqrt 2)^2=\frac{9}{4} \\(ii) (x+\frac{1}{2})^2+(y+\sqrt 2)^2=\frac{9}{4}$

（3）依题意，过点F的直线斜率存在，及直线不与x轴垂直。

既然过x轴上的焦点F(-1,0),且斜率存在，故可设该直线方程为x轴上的截距式，即

$$x = ky-1$$

设直线与交椭圆C于A、B两点，坐标分别为$(x_1,y_1),(x_2,y_2)$.
点P的坐标为$(x_0,y_0)$,
直线代入椭圆C有：

$$ \frac{(ky-1)^2}{2}+y^2=1$$

$$(k^2+2)y^2-2ky-1=0$$

$\therefore y_1+y_2=\frac{2k}{k^2+2}\\ y_1 \cdot y_2 = - \frac{1}{k^2+2}$

$x_1+x_2=k(y_1+y_2)-2=-\frac{4}{k^2+2}$

假设存在点P，使得$\overrightarrow {AP}=\overrightarrow{OB}$,则有

$$(x_0-x_1, y_0-y_1) = (x_2,y_2)\\x_0=x_1+x_2=-\frac{4}{k^2+2},\\ y_0 = y_1+y_2=\frac{2k}{k^2+2}$$

点P在椭圆C上，故有$\frac{x_0^2}{2}+y_0^2=1$,

$\therefore \frac{8}{(k^2+2)^2}+\frac{4k^2}{(k^2+2)^2}=1$

$\therefore (k^2+2)^2 = 8+4k^2 \\k^4=4, k^2=2, k=\pm \sqrt 2$

$\therefore x_0=-1, y_0=\pm \frac{\sqrt 2}{2}$

综上所述，点P有两种可能，分别为$(-1,\frac{\sqrt 2}{2}), (-1, -\frac{\sqrt 2}{2})$.
