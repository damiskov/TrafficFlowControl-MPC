# Overview and Assumptions

- Traffic flows can be modelled as gaseous flows 
- Can measure density.

# State Variables

- Traffic densities
	- 
# Discrete-Time State Equations
## Intersection $1$

$$\mathrm{V}_{1} = \begin{bmatrix} v_{21}  &  v_{31}  &  v_{w1}  &  v_{n1} \end{bmatrix}^{\top}$$
$$\begin{align}\\
v^{k+1}_{21}&= v^{k}_{21}−\delta^{k}_{1} \alpha_{21} v^{k}_{21}+\delta^{k}_{2}\alpha_{e1} v^{k}_{e2}+(1−\delta^{k}_{2})(\alpha_{41}v^{k}_{42} + \alpha_{n1}v^{k}_{n2})\\
v^{k+1}_{31}&= v^{k}_{31}−\delta^{k}_{1}\alpha_{31}v^{k}_{31}+\delta^{k}_{3}\alpha_{s31} v^{k}_{s3}+(1−\delta^{k}_{3})(\alpha_{431} v^{k}_{43} + \alpha_{w31} v^{k}_{w3}) \\
v_{w1}^{k+1}&= v_{w1}^{k} - \delta_{1}^{k} \alpha_{w1} v_{w1}^{k}+q_{w1} \\
v_{n1}^{k+1}&= v_{n1}^{k} - \left( 1- \delta_{1}^{k} \right) \alpha_{n1} v_{n1}^{k} + q_{n1} 
\end{align}$$