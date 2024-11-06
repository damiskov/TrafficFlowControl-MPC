import numpy as np


class OneIntersectionSystem:
    """
    
    Class for the process system of a single intersection.

    The system consists of 4/4 ingoing/outgoing road segments.
    The system is controlled by adjusting the traffic signal control, which is implemented as a "valve".

    Note - The class will work with PRESENT system state, but will not store the historical states.
    - Historical states must stored in the main program.
    """

    def __init__(self, params, initial_state) -> None:
        """
        Constructor for the OneIntersectionSystem class.
        - Define parameters of the system.
        - Set initial state.

        Parameters:
            params (dict): Dictionary containing the parameters of the system.
                - a (float): Rates of left/right turn. [N/A]
                - b (float): Rate of continuing straight. [N/A]
                - v (float): velocity of cars at intersection - assumed constant. [L/T]
                - beta (4x1 np.ndarray): Weird constant. [1/L]
                - d (4x1 np.ndarray): External flow rate. [M/(L^3T)]
            x_init (np.ndarray): Initial state of the system - Initial incoming traffic densities.
        """
        print(f"Initializing OneIntersectionSystem with parameters:")
        for key, value in params.items():
            print(f"{key}: {value}")
        
        print(f"Initial state:\n{initial_state}")
        
        self.a = params['a']
        self.b = params['b']
        self.v = params['v']
        self.beta = params['beta']
        self.d = params['d']
        
        self.P = initial_state
    

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
        return self.P
    
    
    def sensor(self) -> np.ndarray:
        """
        Returns the sensor measurement for the current state.

        I.e., the density flow rate of incoming road segments.

        drho/dt = rho*v*beta

        """
        y = np.multiply((self.P*self.v), self.beta)
        print(f"Sensor measurement: {y}")
        return y
    
    def output(self) -> np.ndarray:
        """
        Returns the output of the system.

        (same as sensor for now?)
        """
        return self.sensor()


    
    def process(self, t, x, delta):
        """
        The process model for our single intersection system.

        Parameters:
            t (float): Time.
            rho (np.ndarray): State of the system - current densit
            delta (np.ndarray): Control input.
        
        Returns:
            dxdt (np.ndarray): Derivative of the state (mass) w.r.t time.
        """

        # ODE

        # Outgoing flow rates

        q_N1 = - ((1-delta)*self.P[0]*self.v)
        q_E1 = - (delta*self.P[1]*self.v)
        q_S1 = - ((1-delta)*self.P[2]*self.v)
        q_W1 = - (delta*self.P[3]*self.v)

        # Incoming flow rates
        p_N1 = self.d[0]
        p_E1 = self.d[1]
        p_S1 = self.d[2]
        p_W1 = self.d[3]

        # Derivative of the state
        dPdt = np.zeros((4,1))

        dPdt[0] = p_N1 - q_N1
        dPdt[1] = p_E1 - q_E1
        dPdt[2] = p_S1 - q_S1
        dPdt[3] = p_W1 - q_W1
        
        return dPdt

        
    
        

        
        
        

        

