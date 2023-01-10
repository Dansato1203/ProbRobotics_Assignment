import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

from Dist_of_FinishRate import Bayes_theorem

class Plot_Compare_graph:
	def __init__(self):
		self.Before_Posterior_dist_list = []
		self.After_Posterior_dist_list = []

	def Plot(self, x,  graph_name):
		fig = plt.figure()
		ax = SubplotZero(fig, 111)
		fig.add_subplot(ax)

		for direction in ["right", "top"]:
			ax.axis[direction].set_visible(False)
		for direction in ["left",  "bottom"]:
			ax.axis[direction].set_axisline_style("-|>")

		ax.plot(x, self.Before_Posterior_dist_list[-1], label="Before_Trial")
		ax.plot(x, self.After_Posterior_dist_list[-1], label="After_Trial")
		plt.grid()
		ax.set_xlabel('t')
		ax.set_ylabel('Prob')
		ax.legend(loc=0)
		ax.set_xlim(0, 1)
		ax.set_ylim(0, 0.09)

		fig.tight_layout()
		fig.savefig("../image/" + graph_name + ".png", bbox_inches="tight")

def main():
	# 改良前での5回の試行
	Before_Trial = ["完走", "失敗", "失敗", "完走", "完走"]
	# 改良後での5回の試行
	After_Trial = ["完走", "完走", "完走", "完走", "完走"]

	bayes = Bayes_theorem()

	p1 = Plot_Compare_graph()

	# 改良前と改良後の分布を計算
	bayes.Calc_dist(Before_Trial, p1.Before_Posterior_dist_list)
	bayes.Calc_dist(After_Trial, p1.After_Posterior_dist_list)

	p1.Plot(bayes.t, "5_Trial")

	# 試行回数を100回に増やす
	# 改良前での100回の試行
	Before_100_Trial = ["完走", "失敗", "失敗", "完走", "完走"]*20
	# 改良後での100回の試行
	After_100_Trial = ["完走", "完走", "完走", "完走", "完走"]*20

	p2 = Plot_Compare_graph()

	# 改良前と改良後の分布を計算
	bayes.Calc_dist(Before_100_Trial, p2.Before_Posterior_dist_list)
	bayes.Calc_dist(After_100_Trial, p2.After_Posterior_dist_list)

	p2.Plot(bayes.t, "100_Trial")

if __name__ == "__main__":
	main()
