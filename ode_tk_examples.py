from ode_toolkit import *
# ##TEST ZONE
# ODE1 = lambda x: np.array([x[1],-x[0]-x[1]*x[0]**2])
# V1 = lambda x:x[0]**2 +x[1]**2
# ex1 = Analysis(ODE1,2)
# ex1.lyapunov_plot(V1)
# # plt.show() 

# ODE2 = lambda x: np.array([-6*x[0]-4*x[0]**3-2*x[1],-x[0]-x[1]])
# V2 = lambda x:(x[0]+x[1])**2+(x[0]**2+1)**2-1
# ex2 = Analysis(ODE2,2)
# ex2.plot_phase_potrait()
# ex2.lyapunov_plot(V2)
# plt.show()

# def ODE3(x,parameters):
#     t,omega,v_0 = parameters
#     return np.array([np.sin(omega*(t-x[1]/v_0)),np.ones(x[0].shape)*v_0])
# ex3 = Analysis(ODE3,2)
# # ex3.plot_phase_potrait(np.array([10,1]))
# slider_names = ["t","omega","v_0"]
# ex3.parameter_phase_portrait(slider_names)
# plt.show()

# def ODE4(x,parameters):
#     a,b,c,d = parameters
#     return np.array([a*x[0]+b*x[1],c*x[0]+d*x[1]])
# ex4 = Analysis(ODE4,2,[1,2,3,4])
# slider_names = ["a","b","c","d"]
# ex4.parameter_phase_portrait(slider_names)

# def ODE5(x,parameters):
#     t = parameters
#     return np.array([-x[1],x[0]+t])
# ex5 = Analysis(ODE5,2)
# # ex3.plot_phase_potrait(np.array([10,1]))
# slider_names = ["t"]
# ex5.parameter_phase_portrait(slider_names)
# plt.show()


def ODE6(x,parameters):
    a = parameters
    return np.array([x[0]-x[0]**2-a*x[0]*x[1],x[1]-x[1]**2-a*x[0]*x[1]])
ex5 = Analysis(ODE6,2)
# ex3.plot_phase_potrait(np.array([10,1]))
slider_names = ["a"]
ex5.parameter_phase_portrait(slider_names)
plt.show()
