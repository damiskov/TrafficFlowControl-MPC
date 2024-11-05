import numpy as np


class OneIntersectionSystem:
    """
    
    Class for the process system of a single intersection.

    The system consists of 4/4 ingoing/outgoing road segments.
    The system is controlled by adjusting the traffic signal control, which is implemented as a "valve".

    Note - The class will work with PRESENT system state, but will not store the historical states.
    - Historical states must stored in the main program.
    """

    def __init__(self, x_init, params) -> None:
        """
        Constructor for the OneIntersectionSystem class.
        - Define parameters of the system.
        - Set initial state.

        Parameters:
            params (dict): Dictionary containing the parameters of the system.
                - a (float): Rates of left/right turn. [N/A]
                - b (float): Rate of continuing straight. [N/A]
                - v (float): velocity of cars at intersection - assumed constant. [L/T]
                - beta (float): Weird constant. [1/L]
                - rho (float): Density of the water. [g/cm3]
            x_init (np.ndarray): Initial state of the system - Initial incoming traffic densities.
        """
        self.a = params['a']
        self.b = params['b']
        self.v = params['v']
        self.beta = params['beta']
        self.rho = params['rho']
        
        # Dimension check
        assert x_init.shape == (4,1), "Initial state must be a 4x1 vector"

        self.x = x_init
    

    def __str__(self) -> None:
        """
        Pretty print the system parameters.
        """
        pass
        

 
    def get_state(self) -> np.ndarray:
        """
        Returns the state of the system.
            - The density of incoming road segments.
        """
        return self.x
    
    
    def get_sensor(self) -> np.ndarray:
        """
        Returns the sensor measurement for the current state.

        I.e., the density flow rate of incoming road segments.

        drho/dt = rho*v*beta

        """
        y = self.x * self.v * self.beta
        return y
    
    def get_output(self) -> np.ndarray:
        """
        Returns the output of the system.

        (same as sensor for now?)
        """
        return self.system_sensor()


    
    def process(self, t, x, u):
        """
        The process model for our single intersection system.

        Parameters:
            t (float): Time.
            x (np.ndarray): State of the system - current densit
            u (np.ndarray): Control input.
        
        Returns:
            dxdt (np.ndarray): Derivative of the state (mass) w.r.t time.
        """




        # # Update state
        # self.x=x 
        # self.h = self.m / (self.rho * self.A) # Update heights
        # F = u
       
        
        # qout = np.sqrt(2 * self.g * self.h) * self.a # Outflow of each tank (cm3/s)

        # # Calculating in flows [cm3/s]

        # qin = np.zeros(4)
        # qin[0] = F[0]*self.gamma[0] # valve 1 -> tank 1
        # qin[1] = F[1]*self.gamma[1] # valve 2 -> tank 2
        # qin[2] = F[1]*(1-self.gamma[1]) # valve 2 -> tank 3
        # qin[3] = F[0]*(1-self.gamma[0]) # valve 1 -> tank 4

        # # ODE - Mass balance
        # dxdt = np.zeros(4)
        # dxdt[0] = self.rho*(qin[0]+qout[2]-qout[0])
        # dxdt[1] = self.rho*(qin[1]+qout[3]-qout[1])
        # dxdt[2] = self.rho*(qin[2]-qout[2])
        # dxdt[3] = self.rho*(qin[3]-qout[3])

        return dxdt

        
    
        

        
        
        

        

