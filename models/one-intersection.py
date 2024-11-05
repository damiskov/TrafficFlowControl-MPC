"""
Class for the 4-tank system

Author: David Miles-Skov
Date: 25/09/2024
"""
import numpy as np


class OneIntersectionSystem:
    """
    
    Class for the process system of a single intersection.

    The system consists of 4/4 ingoing/outgoing road segments.
    The system is controlled by adjusting the traffic signal control, which is implemented as a "valve".

    Note - The class will work with PRESENT system state, but will not store the historical states.
    - Historical states must stored in the main program.
    """

    def __init__(self, params) -> None:
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
        """
    

    def __str__(self) -> None:
        """
        Pretty print the system parameters.
        """
        
    

        
        

    def set_initial_condition(self, x0):
        """
        Set the initial condition (mass) of the system.
        - Also sets the initial height of the water in the tanks.
        """
        self.m = x0
        self.h = self.m / (self.rho * self.A)

    def update_system(self, u: np.ndarray) -> np.ndarray:
        """
        Updates the system state.
        """
        pass

    def get_state(self) -> np.ndarray:
        """
        Returns the state (mass) of the system.
        """
        return self.m
    
    
    def system_sensor(self, x) -> np.ndarray:
        """
        Returns the sensor measurement for the current state.

        I.e., the height of the water in all 4 tanks.
        """
        
        return x/(self.rho*self.A)
    
    def system_output(self, x) -> np.ndarray:
        """
        Returns the output of the system.

        I.e., the height of water in tanks 1 and 2.
        """
        H = x/(self.rho*self.A)
        return H[0:2]
    
    def process(self, t, x, u):
        """
        The process model for the 4-tank system.

        Parameters:
            t (float): Time.
            x (np.ndarray): State of the system.
            u (np.ndarray): Control input.
        
        Returns:
            dxdt (np.ndarray): Derivative of the state (mass) w.r.t time.
        """

        # Check if input mass is negative, if so, set to zero
        if np.any(x<0):
            print("Negative mass detected, setting to zero")
            x = np.maximum(0, x)
         
        self.m=x 
        self.h = self.m / (self.rho * self.A) # Update heights
        F = u
       
        
        qout = np.sqrt(2 * self.g * self.h) * self.a # Outflow of each tank (cm3/s)

        # Calculating in flows [cm3/s]

        qin = np.zeros(4)
        qin[0] = F[0]*self.gamma[0] # valve 1 -> tank 1
        qin[1] = F[1]*self.gamma[1] # valve 2 -> tank 2
        qin[2] = F[1]*(1-self.gamma[1]) # valve 2 -> tank 3
        qin[3] = F[0]*(1-self.gamma[0]) # valve 1 -> tank 4

        # ODE - Mass balance
        dxdt = np.zeros(4)
        dxdt[0] = self.rho*(qin[0]+qout[2]-qout[0])
        dxdt[1] = self.rho*(qin[1]+qout[3]-qout[1])
        dxdt[2] = self.rho*(qin[2]-qout[2])
        dxdt[3] = self.rho*(qin[3]-qout[3])

        return dxdt

        
    
        

        
        
        

        

