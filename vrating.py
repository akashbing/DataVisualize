from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.layouts import layout
from bokeh.models import Toggle, BoxAnnotation, CustomJS
output_file("vrating.html")

months = ['jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']
V = ['v1', 'v2', 'v3','v4']

data = {'months' : months,
        'v1'   : [2, 1, 4, 3, 2, 4, 8, 6, 9 , 10, 2, 3],
        'v2'   : [5, 3, 3, 2, 4, 6, 7, 6, 9, 10, 1, 4],
        'v3'   : [3, 2, 4, 4, 5, 3, 6, 9, 8, 7, 3, 4],
        'v4'   : [5, 3, 3, 4, 5, 3, 6, 2, 3, 10, 2, 3] }

source = ColumnDataSource(data=data)

p = figure(x_range=months, y_range=(0, 10), plot_height=500, title="Rating by months",
           toolbar_location=None, tools="")

x=p.vbar(x=dodge('months', -0.30, range=p.x_range), top='v1', width=0.2, source=source,
       color="#c9d9d3", legend=value("v1"))

y=p.vbar(x=dodge('months',  -0.10,  range=p.x_range), top='v2', width=0.2, source=source,
       color="#718dbf", legend=value("v2"))

z=p.vbar(x=dodge('months',  0.10, range=p.x_range), top='v3', width=0.2, source=source,
       color="#e84d60", legend=value("v3"))
a=p.vbar(x=dodge('months',  0.30, range=p.x_range), top='v4', width=0.2, source=source,
       color="pink", legend=value("v4"))
p.add_tools(HoverTool(tooltips=[("vehicle1", "@v1"), ("vehicle2", "@v2"),("vehicle3", "@v3"),("vehicle4", "@v4")]))

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

# We write coffeescript to link toggle with visible property of box and line
code = '''\
object.visible = toggle.active
'''

callback1 = CustomJS.from_coffeescript(code=code, args={})
toggle1 = Toggle(label="vehicle1", button_type="success", callback=callback1,width=1)
callback1.args = {'toggle': toggle1, 'object': x}

callback2 = CustomJS.from_coffeescript(code=code, args={})
toggle2 = Toggle(label="vehicle2", button_type="success", callback=callback2,width=10)
callback2.args = {'toggle': toggle2, 'object': y}

callback3 = CustomJS.from_coffeescript(code=code, args={})
toggle3 = Toggle(label="vehicle3", button_type="success", callback=callback3,width=19)
callback3.args = {'toggle': toggle3, 'object': z}

callback4 = CustomJS.from_coffeescript(code=code, args={})
toggle4 = Toggle(label="vehicle4", button_type="success", callback=callback4,width=28)
callback4.args = {'toggle': toggle4, 'object': a}

output_file("styling_visible_annotation_with_interaction.html")

show(layout([p], [toggle1,toggle2,toggle3,toggle4]))
#show(p)
