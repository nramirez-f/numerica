import matplotlib.pyplot as plt

def function(f,
         x, 
         label='f',
         xlabel='x', 
         ylabel='f(x)',
         title='',
         window_title='Numerica - Function Plot',
         grid=True):

    fig, ax = plt.subplots()

    ax.plot(x, f(x), label=label)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    ax.grid(grid)

    fig.canvas.manager.set_window_title(window_title)

    plt.show()

    return fig