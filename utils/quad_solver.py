import numpy as np
import daqp
from ctypes import * 
import ctypes.util

def quadprog(H, g, l, u, A, bl, bu, xinit ,sense=None):
    """
    Quadratic programming solver for MPC optimization problem

    Minimize: 1/2 x^T H x + g^T x
    Subject to: l <= x <= u
                bl <= A x <= bu

    Parameters
    ----------
    H : array_like
        Quadratic cost matrix
    f : array_like
        Linear cost vector
    A : array_like
        Linear inequality constraint matrix
    b : array_like 
        Linear inequality constraint vector
    lb : array_like 
        Lower bound vector
    ub : array_like 
        Upper bound vector
    x0 : array_like
        Initial guess for the solution

    Returns
    -------
    x : array_like
        Optimal solution
    info : dict
        Information about the optimization problem
        (fval, exitflag, info) see daqp.solve for more details         
    """
    if sense is None:
        sense = np.zeros((A.shape[0]+bl.shape[0]), dtype=c_int) # determines the type of constraints


    # Vertically stack the lower and upper bounds - Necessary for daqp interface
    blower = np.concatenate((l, bl), axis=0)
    bupper = np.concatenate((u, bu), axis=0) 

    # Check shapes
    assert H.shape[0] == H.shape[1], 'H must be a square matrix'
    assert H.shape[0] == g.shape[0], 'H and g must have the same number of rows'
    assert A.shape[1] == H.shape[0], 'A and H must have the same number of columns'
    assert A.shape[0] == bl.shape[0], 'A and bl must have the same number of rows'
    assert A.shape[0] == bu.shape[0], 'A and bu must have the same number of rows'
    assert bl.shape[0] == bu.shape[0], 'bl and bu must have the same number of rows'
    assert l.shape[0] == u.shape[0], 'l and u must have the same number of rows'



    xstar, fval, exitflag, info = daqp.solve(H,g,A,bupper,blower,sense)

    info = {'fval' : fval, 'exitflag' : exitflag, 'info' : info}


    return xstar, info