import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

# 事前分布を求める
def Prior_dist():
	return np.full(101, 1/101)

# p(a|t)を求める
def P_a_t(a, Finish_rate):
	if a == "完走":
		return Finish_rate
	elif a == "失敗":
		return np.ones(101) - Finish_rate

# 事後分布を求める
def Posterior_dist(P_a_t, Prior_dist):
	return  P_a_t * Prior_dist / sum(P_a_t * Prior_dist)

# 離散化したt
t = []
for i in range(0, 101, 1):
	t.append(i / 100)

# 改良前での5回の試行
Before_Trial = ["完走", "失敗", "失敗", "完走", "完走"]
# 改良後での5回の試行
After_Trial = ["完走", "完走", "完走", "完走", "完走"]

Posterior_dist_list = []
prior_dist = Prior_dist() # 事前分布
Posterior_dist_list.append(prior_dist) #プロットするために記録

# 試行ごとに計算
for trial in Before_Trial:
	p_a_t = P_a_t(trial, t) # P(a|t)を計算
	posterior_dist = Posterior_dist(p_a_t, prior_dist) # 事前分布とP(a|t)から事後分布を計算
	prior_dist = posterior_dist # i回目までの試行を反映したP(t|a_1:t)を事前分布とみなす
	Posterior_dist_list.append(posterior_dist) # プロット用に記録

# 試行ごとのtの分布をプロット
ax = [0]*6
x = t
Title_list = ["Before Experiment", "1st Trial (Success)", "2nd Trial (Fail)", "3rd Trial (Fail)", "4th Trial (Success)", "5th Trial (Sucess)"]

fig = plt.figure(figsize=(14, 10))

for i in range(6):
	y = Posterior_dist_list[i]
	ax[i] = SubplotZero(fig, 2, 3, i+1)
	fig.add_subplot(ax[i])
	for direction in ["right", "top"]:
		ax[i].axis[direction].set_visible(False)
	for direction in ["left",  "bottom"]:
		ax[i].axis[direction].set_axisline_style("-|>")
	ax[i].plot(t, y)
	plt.grid()
	ax[i].set_xlabel('t')
	ax[i].set_ylabel('Prob')
	ax[i].set_title(Title_list[i], y = -0.15)
	ax[i].set_xlim(0, 1)
	ax[i].set_ylim(0, 0.09)

fig.tight_layout()
fig.savefig("../image/Before_Trial.png", bbox_inches="tight")


# 改良後
Posterior_dist_list = []
prior_dist = Prior_dist() # 事前分布
Posterior_dist_list.append(prior_dist) #プロットするために記録

# 試行ごとに計算
for trial in After_Trial:
	p_a_t = P_a_t(trial, t) # P(a|t)を計算
	posterior_dist = Posterior_dist(p_a_t, prior_dist) # 事前分布とP(a|t)から事後分布を計算
	prior_dist = posterior_dist # i回目までの試行を反映したP(t|a_1:t)を事前分布とみなす
	Posterior_dist_list.append(posterior_dist) # プロット用に記録

ax = [0]*6

for i in range(6):
	y = Posterior_dist_list[i]
	ax[i] = SubplotZero(fig, 2, 3, i+1)
	fig.add_subplot(ax[i])
	for direction in ["right", "top"]:
		ax[i].axis[direction].set_visible(False)
	for direction in ["left",  "bottom"]:
		ax[i].axis[direction].set_axisline_style("-|>")
	ax[i].plot(t, y)
	plt.grid()
	ax[i].set_xlabel('t')
	ax[i].set_ylabel('Prob')
	ax[i].set_title(Title_list[i], y = -0.15)
	ax[i].set_xlim(0, 1)
	ax[i].set_ylim(0, 0.09)

fig.tight_layout()
fig.savefig("../image/After_Trial.png", bbox_inches="tight")
