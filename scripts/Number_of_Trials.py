import numpy as np
import matplotlib.pyplot as plt

# 完走率を求める関数
def Calc_FinishRate(Trial_list):
	success_cnt = 0
	for i in Trial_list:
		if i == "完走":
			success_cnt += 1

	t = success_cnt / len(Trial_list)
	return t

def main():
	print("試行回数 : 5回")
	# 改良前での試行
	Before_Trial = ["完走", "失敗", "失敗", "完走", "完走"]
	# 改良後での試行
	After_Trial = ["完走", "完走", "完走", "完走", "完走"]

	# 改良前
	t = Calc_FinishRate(Before_Trial)
	print(f"改良前の完走率 : {t}")

	# 改良後
	t = Calc_FinishRate(After_Trial)
	print(f"改良後の完走率 : {t}")


	# もう一回試行しただけでこのtの値は大きく変わる
	# 改良前に"完走"を、改良後に"失敗"の試行を追加して完走率を計算してみる

	# 改良前
	Before_Trial.append("完走")
	t = Calc_FinishRate(Before_Trial)
	print(f"改良前の完走率(完走の試行を追加) : {t}")

	# 改良後
	After_Trial.append("失敗")
	t = Calc_FinishRate(After_Trial)
	print(f"改良後の完走率(失敗の試行を追加): {t}")


	# 試行回数を増やすと、一回試行を増やしただけでは完走率は変わらないのでは？
	# 試行回数を15回に増やしてみる
	print("\n")
	print("試行回数 : 15回")

	Before_Trial = ["完走", "失敗", "失敗", "完走", "完走"]
	After_Trial = ["完走", "完走", "完走", "完走", "完走"]

	# ここでは単純に5回の試行を20倍して100回の試行とする
	Before_Trial_15 = Before_Trial * 3
	After_Trial_15 = After_Trial * 3

	# 改良前
	t = Calc_FinishRate(Before_Trial_15)
	print(f"改良前の完走率 : {t}")

	# 改良後
	t = Calc_FinishRate(After_Trial_15)
	print(f"改良後の完走率 : {t}")

	# 同様に改良前に"完走"を、改良後に"失敗"の試行を追加して完走率を計算してみる
	# 改良前
	Before_Trial_15.append("完走")
	t = Calc_FinishRate(Before_Trial_15)
	print(f"改良前の完走率(完走の試行を追加) : {t}")

	# 改良後
	After_Trial_15.append("失敗")
	t = Calc_FinishRate(After_Trial_15)
	print(f"改良後の完走率(失敗の試行を追加) : {t}")

	# 試行回数を100回に増やしてみる
	print("\n")
	print("試行回数 : 100回")

	Before_Trial = ["完走", "失敗", "失敗", "完走", "完走"]
	After_Trial = ["完走", "完走", "完走", "完走", "完走"]

	# ここでは単純に5回の試行を20倍して100回の試行とする
	Before_Trial_100 = Before_Trial * 20
	After_Trial_100 = After_Trial * 20

	# 改良前
	t = Calc_FinishRate(Before_Trial_100)
	print(f"改良前の完走率 : {t}")

	# 改良後
	t = Calc_FinishRate(After_Trial_100)
	print(f"改良後の完走率 : {t}")

	# 同様に改良前に"完走"を、改良後に"失敗"の試行を追加して完走率を計算してみる
	# 改良前
	Before_Trial_100.append("完走")
	t = Calc_FinishRate(Before_Trial_100)
	print(f"改良前の完走率(完走の試行を追加) : {t}")

	# 改良後
	After_Trial_100.append("失敗")
	t = Calc_FinishRate(After_Trial_100)
	print(f"改良後の完走率(失敗の試行を追加) : {t}")

if __name__ == "__main__":
	main()
