import numpy as np
import numpy.linalg as lag
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib.widgets import Slider, Button

class Analysis():
    def __init__(self,ODE,d,parameters=None,xrange=(-5,5),yrange=(-5,5)):
        self.ODE = ODE
        self.d = d
        self.xrange = xrange
        self.yrange = yrange
        self.parameters = parameters

    def solve_numerically(self,x_0,T,dt):
        N = x_0.shape[0] 
        r = x_0 
        trajectories = np.zeros((T,N,2))
        trajectories[0,:,:] = x_0
        for i in range(T):
            r += self.ODE(r)*dt
            trajectories[i,:,:] = r
        return trajectories

    def plot_phase_potrait(self,normalise=True,stream=False,axes=None):
        if not axes:
            fig,ax = plt.subplots()
            fig.set_size_inches(5,5)
        else:
            ax = axes
        ax.set(xlim = self.xrange,ylim =self.yrange)
        ax.axis("equal")
        n_vec = 30
        x = np.linspace(self.xrange[0],self.xrange[1],n_vec)
        y = np.linspace(self.yrange[0],self.yrange[1],n_vec)
        X,Y = np.meshgrid(x,y)
        if normalise:
            vecs = self.ODE([X,Y],self.parameters)
            [U,V] = vecs/lag.norm(vecs,axis=0)
        else:
            [U,V] = self.ODE([X,Y],self.parameters)
        if stream:
            s = ax.streamplot(X,Y,U,V)
            return X,Y,ax,s
        else:
            q = ax.quiver(X,Y,U,V)
            return X,Y,ax,q

    def parameter_phase_portrait(self,slider_names,slider_ranges=None,slider_init=None):
        n_sliders = len(slider_names)
        if not slider_ranges:
            slider_ranges = [[-5,5] for i in range(n_sliders)]
        if not slider_init:
            slider_init = [1 for i in range(n_sliders)]
        # Create the figure and the vf that we will manipulate

        self.parameters = slider_init
        X,Y,ax,q = self.plot_phase_potrait()
        # adjust the main plot to make room for the sliders
        plt.subplots_adjust(bottom=0.1*n_sliders)

        # Make a horizontal slider to control alpha
        slider_ax = [None for i in range(n_sliders)]
        sliders = [None for i in range(n_sliders)]
        for i,name in enumerate(slider_names):
            slider_ax[i] = plt.axes([0.25, 0.1+0.05*i, 0.5, 0.03])
            sliders[i] = Slider(
                slider_ax[i],
                label = name,
                valmin=slider_ranges[i][0],
                valmax=slider_ranges[i][1],
                valinit = slider_init[i])


        # The function to be called anytime a slider's value changes
        # def update(val):
        #     vecs = ODE([X,Y],alpha = alpha_slider.val,gamma =gamma_slider.val)
        #     [U,V] = vecs/lag.norm(vecs,axis=0)
        #     q.set_UVC(U,V)
        def update(val):
            self.parameters = [s.val for s in sliders]
            ax.clear()
            X,Y,ax1,q = self.plot_phase_potrait(axes=ax)

        # register the update function with each slider
        for s in sliders:
            s.on_changed(update)
        plt.show()

    def lyapunov_plot(self,V,traj=False,traj_parameters=(np.array([0,0]),100,0.01)):
        fig = plt.figure()
        ax = fig.add_subplot(111,projection="3d")
        ax.set(xlim=self.xrange,ylim=self.yrange)
        n_sample = 30
        x = np.linspace(self.xrange[0],self.xrange[1],n_sample)
        y = np.linspace(self.yrange[0],self.yrange[1],n_sample)
        X,Y =np.meshgrid(x,y)
        Z = V([X,Y])
        # s = ax.plot_surface(X,Y,Z,alpha=0.5)
        c = ax.contour3D(X,Y,Z,30,alpha=0.8,cmap="Greys")
        ##generating and normalising vector field
        v_field = np.moveaxis(self.ODE([X,Y]),0,2)
        norms = lag.norm(v_field,axis=2)
        norms = np.moveaxis([norms,norms],0,2)
        v_field = v_field/(2*norms)
        q = ax.quiver(X,Y,np.zeros(X.shape),v_field[:,:,0],v_field[:,:,1],np.zeros(X.shape))
        ##plotting trajectories
        if traj:
            x_0,T,dt = traj_parameters
            traj = self.solve_numerically(x_0,T,dt)
        return fig,ax
