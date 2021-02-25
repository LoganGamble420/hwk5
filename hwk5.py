import numpy as np
import matplotlib.pyplot as plt

def f(x):
    ''' function to be evaluated'''
    return x**2

def integral_f(x):
    ''' analytical integral of  f(x) '''
    return (x**3)/3

def left_sum(x,y):
    ''' Function that takes in values of x and f(x), and calculates the reimann             sum using a left value approximation '''
    area=[]
    for i in range(len(x[:-1])):
        a=y[1] * (x[i+1]-x[i])
        area.append(a)
        answer=0
    for l in area:
        answer += l
    return answer

def trap_sum(x,y):
    ''' Function that takes in x and f(x) and calculates the reimann sum using a            trapezoidal value approximation''' 
    area=[]
    for i in range(len(x[:-1])):
        side1=y[i]
        side2=y[i+1]
        a = 0.5 * (side1 + side2) * (x[i+1] - x[i])
        area.append(a)
    answer = 0
    for t in area:
        answer += t
    return answer

def sim_sum(func,x,y,h):
    ''' Function that computes simpsons rule'''
    sim_range=np.arange(x,y,h)
    n=sim_range[1]-sim_range[0]
    ans=0
    for i in sim_range:
        ans += (f(i-n) + 4*f(i) + f(i+n)) * h/6
    return ans

def error_calc(true,calc):
    ''' Function that computes the relative error'''
    return ((true-calc)/true) * 100

if __name__ == '__main__':
    many_h=[.1,.01,.001,.0001,.00001,.000001]
    left_sum_list=[]
    trap_sum_list=[]
    sim_sum_list=[]
    processes=[]
    for h in many_h:
        x=np.arange(0,1,h)
        y=f(x)
        processes.append(len(x))
        l_sum = left_sum(x,y)
        l_error = error_calc(integral_f(1), l_sum)
        left_sum_list.append(l_error)
        t_sum=trap_sum(x,y)
        t_error = error_calc(integral_f(1), t_sum)
        trap_sum_list.append(t_error)
        s_sum=sim_sum(f, 0, 1, h)
        s_error=error_calc(integral_f(1), s_sum)
        sim_sum_list.append(s_error)

plt.plot(left_sum_list, label = 'Upper Sum')
plt.plot(trap_sum_list, label = 'Trapezoid Sum')
plt.plot(sim_sum_list, label = 'Simpsons Sum')
plt.legend()
plt.title('How different numerical integration methods differ')
plt.xscale=('log')
plt.xlabel('steps')
plt.ylabel('error')
plt.show()

#not sure what happened with my left_sum i tried for a while to fix it

