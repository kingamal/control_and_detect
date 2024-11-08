from motion_detector import df
from bokeh.plotting import figure, show, output_file

p=figure(x_axis_type='datetime', height=100, width=500, resizable=True, title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid.ticker = [0,1]

q=p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")

output_file("Graph.html")
show(p)