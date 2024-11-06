import numpy as np


class BasicController:
    """
    Class containing the basic controller functions. Allows for the controller to be
    have "memory" of the previous control input and the previous state.
    - Each method just needs to be called with the current state and the reference value.
    - Must remember to update the previous control input and the previous state after each iteration.

    Parameters:
    -----------
        Kp (float): Proportional gain.
        Ki (float): Integral gain.
        Kd (float): Derivative gain.
        umin (float): Minimum control input.
        umax (float): Maximum control input.
    
    Available methods:
    ------------------
        p_controller: Proportional controller.
        pi_controller: Proportional-Integral controller.
        pid_controller: Proportional-Integral-Derivative controller.
    """

    def __init__(self, Kp, Ki, Kd, umin, umax):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.umin = umin
        self.umax = umax
        self.i = np.zeros(2)
        self.z_prev = np.zeros(2)
        self.u_prev = np.zeros(2)


    def p_controller(self, r, z):
        """"

        Proportional controller.

        Parameters:
        -----------
            r (float): Reference value.
            z (float): Current value.
            u_prev (float): Previous control input.
            Kp (float): Proportional gain.
        
        Returns:
        --------
            u (float): Control input.
        """
        v, u = np.zeros_like(self.u_prev), np.zeros_like(self.u_prev)
        v = self.u_prev + self.Kp*(r - z)    
        u = np.maximum(self.umin, np.minimum(self.umax, v))

        if np.any(u)<0:
            raise ValueError("Control input is negative - Not allowed")
        
        
        return u


def pi_controller(i,dt, r, z, u_prev, Kp, Ki, umin, umax):
    """

    Proportional-Integral controller.
    
    Parameters:
    ----------
        r (float): Reference value.
        z (float): Current value.
        u_prev (float): Previous control input.
        Kp (float): Proportional gain.
        Ki (float): Integral gain.

    Returns:
    --------
        u (float): Control input.
    """
    v, u = np.zeros_like(u_prev), np.zeros_like(u_prev)

    i_new = i + Ki*dt*(r - z)
    v = u_prev + Kp*(r - z) + i_new
    
    # Saturation based anti wind up

    # if np.any(v > umax) or np.any(v < umin):
    #     i_new = i 

    u = np.maximum(umin, np.minimum(umax, v))

    
    return u, i_new


def pid_controller(i,dt, r, z,z_prev, u_prev, Kp, Ki,Kd, umin, umax):
    """
    Proportional-Integral-Derivative controller.
    """
    e = r - z
    i_new = i + Ki*dt*e
    # v = u_prev + Kp*(e) + Kd*(z-z_prev)/dt + i_new
    v = u_prev + Kp*(r - z) + Ki*dt*i - Kd*(z-z_prev)/dt
    # Saturation based anti wind up
    # if np.any(v > umax) or np.any(v < umin):
    #     i_new = i 
    u = np.maximum(umin, np.minimum(umax, v))
    if np.any(u)<0:
        raise ValueError("Control input is negative")

    return u, i_new