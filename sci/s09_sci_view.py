"""

Enable Scientific Mode

- Editor / Interactive Console / Documentation / SciView
- Execute cells inside Interactive Console
- Inspect scientific arrays (numpy arrays, pandas DataFrames, pandas Series) in Data Viewer
- Inspect plots under 'Plots' tab

"""

#%%

from matplotlib.pylab import figure, plot, xlabel, ylabel, title, show, subplot, np

#%%

x = np.linspace(0, 5, 10)
y = x ** 2

#%%

figure()
plot(x, y, 'r')
xlabel('x_zero')
ylabel('y')

title('title')
show()

#%%

subplot(1, 2, 1)
plot(x, y, 'r--')
subplot(1, 2, 2)
plot(y, x, 'g*-')
show()

#%%

fig = figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
show()
