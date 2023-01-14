from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('simple_graphed.html')
    fig = figure()
    
    total_vals = int(input('How many values would you like to graph out: '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Value and what for {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)






