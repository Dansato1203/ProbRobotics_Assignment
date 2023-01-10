# ProbRobotics_Assignment
確率ロボティクスの課題提出用のリポジトリ

## 作成したプログラムによる結果
### Number_of_Trials.py
C君が行った5回の試行の結果を信頼できるか検証するプログラム．  
```Calc_FinishRate```関数によって完走率を計算する．  
https://github.com/Dansato1203/ProbRobotics_Assignment/blob/543ffeed90a6d8f2c568c0b45ac471ec360f10fb/scripts/Number_of_Trials.py#L5-L12
<br>
試行は改良前と改良後でそれぞれ以下の通りとした．  
- 改良前 : ["完走", "失敗", "失敗", "完走", "完走"]
- 改良後 : ["完走", "完走", "完走", "完走", "完走"]  
  
改良前と改良後での5回の試行による完走率を求めると以下の結果が得られた．  
|  　  |  完走率  |
| ---- | ---- |
|  改良前  |  0.6  |
|  改良後  |  1.0  |
<br>
次に，もう一回試行を追加した場合の完走率の値を求める．  
改良前に"完走"，改良後に"失敗"の試行を追加したのちに完走率を計算すると以下の結果が得られた．  
|  　  |  完走率  |
| ---- | ---- |
|  改良前  |  0.667  |
|  改良後  |  0.833  |
  
追加前は改良の前後で0.4あった完走率の差が0.178程度となる結果となった．  
<br>
そこで，試行の回数を15回，100回に増やして同様の検証を行う．  
試行はの5回の試行を単純に3倍，20倍として15回，100回の試行とする．  
まず，試行回数を15回として検証を行った．  
同様に改良前に"完走"，改良後に"失敗"の試行を追加したのちに完走率を計算すると以下の結果が得られた．  
|  　  |  完走率  |
| ---- | ---- |
|  改良前  |  0.625  |
|  改良後  |  0.9375  |
  
15回の試行にさらに試行を一回追加した場合には，完走率の差は0.3程度であり，試行の追加前とは0.1 程度の差である結果となった．  
<br>
次に，試行回数を100回に増やし，更に試行を一回追加した場合には以下の結果が得られた．  
|  　  |  完走率  |
| ---- | ---- |
|  改良前  |  0.604  |
|  改良後  |  0.99   |
  
100回の試行の場合には，完走率のは0.39程度となり，試行の追加前とは0.01程度の差となった．  
<br>  
以上の結果から，5回のみの試行では，一回の試行によって結果が大きく変わるため結果を信頼できないと考えられる．  
また，15回，100回と試行の回数を増やすにつれ，試行の追加の前後で完走率の差は小さくなったため，試行回数はより多いほうが望ましいといえる．  
15回試行の場合では，試行の追加前後で完走率の差が0.1程度になったため，最低15回は試行を行うべきだと考える．  
　　
### Dist_of_FinishRate.py  
完走率tの分布の遷移を求めるプログラム 
```Bayes_theorem```クラスによって施行後の確率分布を計算する．  
```Bayes_theorem```クラス中の```Prior_dist```関数によって事前分布を計算する．  
https://github.com/Dansato1203/ProbRobotics_Assignment/blob/543ffeed90a6d8f2c568c0b45ac471ec360f10fb/scripts/Dist_of_FinishRate.py#L13-L14
  
また，```Bayes_theorem```クラス中の```P_a_t```関数によってP(a|t)を計算する．  
https://github.com/Dansato1203/ProbRobotics_Assignment/blob/543ffeed90a6d8f2c568c0b45ac471ec360f10fb/scripts/Dist_of_FinishRate.py#L17-L21

```Prior_dist```関数と```P_a_t```関数によって計算された事前分布とP(a|t)から```Posterior_dist```関数によって計算する．  
https://github.com/Dansato1203/ProbRobotics_Assignment/blob/543ffeed90a6d8f2c568c0b45ac471ec360f10fb/scripts/Dist_of_FinishRate.py#L24-L25
  
```Calc_dist```関数では，i回目までの試行によって事前分布を更新して試行ごとに確率分布を求める．  
  
5回の試行は同様に以下の通りとする．  
- 改良前 : ["完走", "失敗", "失敗", "完走", "完走"]
- 改良後 : ["完走", "完走", "完走", "完走", "完走"]  
  
改良前の試行による完走率の確率分布は以下の通りとなった．  
<img src="https://github.com/Dansato1203/ProbRobotics_Assignment/blob/main/image/02_Before_Trial.png" width="600">  
また，改良後の試行による完走率の確率分布は以下の通りとなった．  
<img src="https://github.com/Dansato1203/ProbRobotics_Assignment/blob/main/image/02_After_Trial.png" width="600">
  
### Comparison_of_Dist.py
改良の前後での確率分布の比較を行うプログラム  
```Dist_of_FinishRate.py```で作成した```Bayes_theorem```クラスによって確率分布を求め，改良の前後での確率分布を比較する．  
試行回数が5回の際の分布は以下の通りとなった．  
