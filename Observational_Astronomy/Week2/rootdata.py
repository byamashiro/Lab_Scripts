import ROOT
import numpy as np
from rootpy.plotting import Canvas, Graph
from rootpy.plotting.style import get_style, set_style
from rootpy.interactive import wait
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


#anna
anna_h = np.array([161,165,163,174,171,169])
anna_h_d = np.array([5,5,5,5,5,5])

anna_w = np.array([165,177,157,173,175,183])
anna_w_d = np.array([5,5,5,5,5,5])

#randy
randy_h = np.array([176.0,172.5,172.1,161.3,174.0,162.5,171.2,161.5])
randy_h_d = np.array([0.1,0.2,0.2,0.1,0.2,0.1,0.2,0.1])

randy_w = np.array([179.2,184.0,175.7,160.5,174.0,158.0,169.8,164.0])
randy_w_d = np.array([0.2,0.1,0.2,0.1,0.2,0.2,0.2,0.2])

#james
james_h = np.array([171.6,176.0,176.7,161.3])
james_h_d = np.array([0.2,0.2,0.2,0.2])

james_w = np.array([174.7,177.8,174.1,166.1])
james_w_d = np.array([3.5,3.5,3.5,3.3])

#bryan
bryan_h = np.array([161,172,163])
bryan_h_d = np.array([1,1,1])

bryan_w = np.array([167,185,161])
bryan_w_d = np.array([1,1,1])

#jacob
jacob_h = np.array([171.9,163.7,176.3,162.4,177.8,161.2])
jacob_h_d = np.array([0.1,0.1,0.1,0.1,0.1,0.1])

jacob_w = np.array([183.6,160.3,178.6,161.3,172.9,165.2])
jacob_w_d = np.array([0.1,0.1,0.1,0.1,0.1,0.1])

#gabster
gabster_h = np.array([175.5,173.1,163.5])
gabster_h_d = np.array([0.1,0.1,0.1])

gabster_w = np.array([171.6,183.9,162.1])
gabster_w_d = np.array([0.2,0.2,0.2])



# set the random seed
ROOT.gRandom.SetSeed(42)
np.random.seed(42)

# points
x = np.sort(np.random.random(10)) * 3500
y = np.random.random(10)

# set style for ROOT
set_style('ATLAS')

# create graph
graph = Graph(x.shape[0])
for i, (xx, yy) in enumerate(zip(x, y)):
    graph.SetPoint(i, xx, yy)

#graph = Graph(x.shape[0])


# set visual attributes
graph.linecolor = 'blue'
graph.markercolor = 'blue'
graph.xaxis.SetTitle("E_{T} [GeV]")
graph.yaxis.SetTitle("d#sigma_{jet}/dE_{T,jet} [fb/GeV]")
graph.xaxis.SetRangeUser(0, 3500)
graph.yaxis.SetRangeUser(0, 1)

# plot with ROOT
canvas = Canvas()
graph.Draw("APL")

label = ROOT.TText(0.4, 0.8, "ROOT")
label.SetTextFont(43)
label.SetTextSize(25)
label.SetNDC()
label.Draw()
canvas.Modified()
canvas.Update()

# plot with matplotlib



#def plot_with_matplotlib():
#    fig, axes = plt.subplots()
#
#    axes.plot(x, y, 'o-', markeredgewidth=0)
#    axes.set_xlabel(r"$E_T$ [GeV]",
#                    horizontalalignment="right", x=1, labelpad=20)
#    axes.set_ylabel(r"$d\sigma_{jet}/dE_{T,jet}$ [fb/GeV]",
#                    horizontalalignment="right", y=1, labelpad=32)
#    axes.set_xlim(0, 3500)
#    axes.set_ylim(0, 1)
#
#    return fig, axes



## plot without style
#
#
#fig1, axes1 = plot_with_matplotlib()
#axes1.text(0.4, 0.8, 'matplotlib (no style)',
#           verticalalignment='center', horizontalalignment='center',
#           transform=axes1.transAxes, fontsize=20)
#
## plot with ATLAS style
#set_style('ATLAS', mpl=True)
#fig2, axes2 = plot_with_matplotlib()
#axes2.text(0.4, 0.8, 'matplotlib',
#           verticalalignment='center', horizontalalignment='center',
#           transform=axes2.transAxes, fontsize=20)
#axes2.xaxis.set_minor_locator(AutoMinorLocator())
#axes2.yaxis.set_minor_locator(AutoMinorLocator())
#
#if not ROOT.gROOT.IsBatch():
#    plt.show()
#
# wait for you to close the canvas before exiting
wait(True)