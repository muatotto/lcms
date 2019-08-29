import matplotlib.pyplot as plt
from statistics import mean, stdev
import os
from matplotlib.backends.backend_pdf import PdfPages

f = open('config', 'r')
config_data = f.readlines()
filename = config_data[0].strip()
strain_name = config_data[1].strip().split(',')
od = config_data[2].strip().split(',')
strain_od = []
for value in od:
	strain_od.append(float(value))
num = config_data[3].strip().split(',')
strain_num = int(num[0])
sample_num = int(num[1])
f.close()

# File open
lcms_data = open("dat/"+filename, "r", encoding="shift-jis")

# Extract MS data
sample_list = []
each_list = []
name_list = []
lines = lcms_data.readlines()
table = sample_num+4#表の上3行と下空白1行分
metabolite_id = 0
n = sample_num / strain_num

for i in range(len(lines)):
	#表の2行目から代謝物名を抽出してname_listに追加
	if(i%table==1):
		name = lines[i].split("\t")
		name[1] = name[1].strip()
		name_list.append(name[1])
	#分析データがない行の処理は飛ばす
	if(i%table>=sample_num+3 or i%table<=2):
		continue
	#分析データがある行の処理
	data = lines[i].split("\t")
	for j in range(len(data)):
		data[j] = data[j].strip()
	each_list.append([int(i/table), int(data[0]), float(data[6])])
	#分析データの一番最後の行まできたらeach_listに入れたデータをsample_listに追加
	if(i%table==sample_num+2):
		sample_list.append(each_list)
		each_list = []

# File close
lcms_data.close()

#Generate data for bar graph
graph_data = []
strain_data = []
cal = []

for i in range(len(name_list)):
	for j in range(sample_num):
		k = int(j/n)
		sample_list[i][j][2] = sample_list[i][j][2]/strain_od[k]
		cal.append(sample_list[i][j][2])
		if(j%n==n-1):
			m = mean(cal)
			sd = stdev(cal)
			strain_data.append([strain_name[k], m, sd])
			cal = []
	graph_data.append([name_list[i], strain_data])
	strain_data = []

#Graph export
if not os.path.exists('img'):
    os.mkdir('img')
colorlist = ['white', 'skyblue', 'midnightblue']
pdf = PdfPages('img/graph_all.pdf')
for i in range(len(graph_data)):
	left = []
	height = []
	eb = []
	for j in range(strain_num):
		left.append(j+1)
		height.append(graph_data[i][1][j][1])
		eb.append(graph_data[i][1][j][2])
	plt.figure(figsize=(5,5), dpi=100).subplots_adjust(left=0.2)
	plt.errorbar(left, height, fmt='none')
	plt.title(graph_data[i][0], fontsize=20)
	plt.ylabel("Relative intensity / $\mathrm{OD_{600}}$", fontsize=15)
	plt.bar(left, height, yerr=eb, capsize=3, width=0.6, tick_label=strain_name, align='center', color=colorlist, edgecolor='black', linewidth=1)
	plt.tick_params(labelsize=18)
	plt.savefig("img/" + str(i) +".png")
	pdf.savefig()
plt.close()
pdf.close()