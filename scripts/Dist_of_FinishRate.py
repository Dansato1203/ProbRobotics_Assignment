import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

class Bayes_theorem:
	def __init__(self):
		# 離散化したt
		self.t = []
		for i in range(0, 101, 1):
			self.t.append(i / 100)

	# 事前分布を求める
	def Prior_dist(self):
		return np.full(101, 1/101)

	# p(a|t)を求める
	def P_a_t(self, a, Finish_rate):
		if a == "完走":
			return Finish_rate
		elif a == "失敗":
			return np.ones(101) - Finish_rate

	# 事後分布を求める
	def Posterior_dist(self, P_a_t, Prior_dist):
		return  P_a_t * Prior_dist / sum(P_a_t * Prior_dist)

	# 試行ごとの分布を計算
	def Calc_dist(self, Trial_list, Posterior_dist_list):
		prior_dist = self.Prior_dist() # 事前分布
		Posterior_dist_list.append(prior_dist) #プロットするために記録

		for idx, trial in enumerate(Trial_list):
			p_a_t = self.P_a_t(trial, self.t) # P(a|t)を計算
			posterior_dist = self.Posterior_dist(p_a_t, prior_dist) # 更新した事前分布とP(a|t)から事後分布を計算
			prior_dist = posterior_dist # i回目までの試行を反映したP(t|a_1:t)を事前分布とみなす
			Posterior_dist_list.append(posterior_dist) # プロット用に記録

# グラフをプロットする
class Plot_graph:
	def __init__(self):
		self.Posterior_dist_list = []
		self.axies_list = [0]*6

	def Plot(self, x, graph_title_list, graph_name):
		fig = plt.figure(figsize=(14, 10))

		for i in range(6):
			self.axies_list[i] = SubplotZero(fig, 2, 3, i+1)
			fig.add_subplot(self.axies_list[i])
			for direction in ["right", "top"]:
				self.axies_list[i].axis[direction].set_visible(False)
			for direction in ["left",  "bottom"]:
				self.axies_list[i].axis[direction].set_axisline_style("-|>")

			y = self.Posterior_dist_list[i]
			self.axies_list[i].plot(x, y)
			plt.grid()
			self.axies_list[i].set_xlabel('t')
			self.axies_list[i].set_ylabel('Prob')
			self.axies_list[i].set_title(graph_title_list[i], y = -0.15)
			self.axies_list[i].set_xlim(0, 1)
			self.axies_list[i].set_ylim(0, 0.09)

		fig.tight_layout()
		fig.savefig("../image/" + graph_name + ".png", bbox_inches="tight")

def main():
	# 改良前での5回の試行
	Before_Trial = ["完走", "失敗", "失敗", "完走", "完走"]
	# 改良後での5回の試行
	After_Trial = ["完走", "完走", "完走", "完走", "完走"]

	bayes = Bayes_theorem()

	# 改良前
	p1 = Plot_graph()

	# 試行ごとに計算
	bayes.Calc_dist(Before_Trial, p1.Posterior_dist_list)

	# 試行ごとのtの分布をプロット
	Title_list = ["Before Experiment", "1st Trial (Success)", "2nd Trial (Fail)", "3rd Trial (Fail)", "4th Trial (Success)", "5th Trial (Sucess)"]
	p1.Plot(bayes.t, Title_list, "02_Before_Trial")

	# 改良後
	p2 = Plot_graph()

	# 試行ごとに計算
	bayes.Calc_dist(After_Trial, p2.Posterior_dist_list)

	# 試行ごとのtの分布をプロット
	Title_list = ["Before Experiment", "1st Trial (Success)", "2nd Trial (Success)", "3rd Trial (Success)", "4th Trial (Success)", "5th Trial (Sucess)"]
	p2.Plot(bayes.t, Title_list, "02_After_Trial")

if __name__ == "__main__":
	main()
