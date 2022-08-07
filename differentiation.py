# %% md
# # Differentiation

# A simple matplotlib based python code to quickly see how a function and it's derivative will look.

# ### v1.0

# %% imports
import matplotlib.pyplot as plt

# %% function definition
def f(x):
    return x

# %% differentiation function
def d(f, x, h):
    return (f(x+h)-f(x))/h

# %% get relevant values from user
h=float(input("Enter the interval for differerntial\n"))
min=float(input("Enter the minimum x value to consider\n"))
max=float(input("Enter the maximum x value to consider\n"))

# %% create data lists to plot
xl=[]
fl=[]
dl=[]
x=min
while (x<max+h):
    xl.append(x)
    fl.append(f(x))
    dl.append(d(f, x, h))
    x+=h

# %% plot f, df
fig, ax=plt.subplots()
ax.grid()
ax.plot(xl, fl, label="f(x)")
ax.plot(xl, dl, label='d f(x)')
ax.legend()

plt.show()