import matplotlib.pyplot as plt

class Scatter():

    def sct_plot(self, x_data, x_axis, y_data, y_axis, title):
        #fig = plt.figure(figsize = [8, 8])
        plt.tick_params(axis='both', direction = "out", labelsize = 18)
        plt.title(title, fontsize = 25)
        plt.scatter(x_data, y_data, s=100, color = "black")
        plt.xlabel(x_axis, fontsize = 24)
        plt.ylabel(y_axis, fontsize = 24)
        plt.rcParams['font.family'] = 'Arial' #全体のフォントを設定
        plt.rcParams['font.size'] = 24 #フォントサイズを設定
        plt.rcParams['lines.linewidth'] = 2 # 線の太さ設定
        plt.savefig("figure/"+title+"")
        plt.show()


    def sct_plot_overwrite(self, x_data, x_axis, y_data, y_axis, x_data_2, y_data_2, title):
        fig = plt.figure(figsize = [8, 8])
        plt.tick_params(axis='both', direction = "out", labelsize = 18)
        plt.scatter(x_data, y_data, s=100, color = "black" )
        plt.scatter(x_data_2, y_data_2, s=100, color = "red")
        plt.xlabel(x_axis, fontsize = 30)
        plt.ylabel(y_axis, fontsize = 30)
        plt.legend(["-RNase","+RNase"])
        plt.savefig("figure/"+title+"_overwrite")
        plt.show()
