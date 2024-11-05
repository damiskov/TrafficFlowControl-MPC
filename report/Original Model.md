Based on the paper: "Control of Traffic Signals in a Model Predictive Control Framework" by Kamal et. Al

## System Description and Model Parameters

![[model-fig.png|400]]


- $od:$ Origin-destination classification.
	- $o:\left\{ \text{e}, \text{w}, \text{n}, \text{s} \right\} \cup \left\{ 1,2,3,4 \right\}$
	- $d:\left\{ \text{e}, \text{w}, \text{n}, \text{s}  \right\} \cup \left\{ 1,2,3,4 \right\}$
- $\delta_{i}:$ Binary variable, indicating the state of traffic signal at the $i$th intersection.
	- $\delta_{i}=1$ if flow is allowed in $e-w$ direction.
	- $\delta_{i}=0$ if flow is permitted in $n-s$ direction.
- $q_{od}:$ Rate of incoming traffic to section $od$. (N/T)
- $p_{od}:$ Rate of outgoing traffic. (N/T)
- $v_{od}:$ Traffic *volume* (number of vehicles) on section $od$. Used as the state variable for the macroscopic flow model. (N)
- $V_{i} \in \mathbb{R}^{4}:$ Vector representing all traffic volumes heading towards intersection $i$.
- $a_{i \sigma}:$ Fraction of traffic that goes straight at intersection $i$ from the $\sigma$ direction.
- $b_{i \sigma}:$ Fraction of traffic that turns left or right at the $i$th intersection from the $\sigma$ direction.
	- Note that $a_{i \sigma} +2 b_{i \sigma} = 1$.
- $\beta_{od}:$ Fraction of traffic that leaves section $od$ in one time-step (if corresponding signal is green). 

## Assumptions

- Traffic that goes straight from east-west and west-east is symmetric. 
	- Same applies to north-south and south-north.
- Rate of incoming traffic $q_{\sigma i}$, entering the network from the $\sigma$ horizon and heading towards the $i$th intersection, can be estimated/measured.

## Conversion of Discrete-Time to Continuous-Time

The state equation of section $od$ can be written, in terms of step counter $k$, as 
$$\begin{align}
v_{od}^{k+1}&=  v_{od}^{k}-p_{od}^{k}+q_{od}^{k}\\
\implies v_{od}^{k+1} - v_{od}^{k} &= -p_{od}^{k}+q_{od}^{k}
\end{align}$$
If we allow the continuous form of the traffic flow rates to take the same variable names, we end up with the following continuous time description for the net flow rate
$$
\frac{d v_{od}}{d t}(t) = -p_{od}(t)+q_{od}(t)
$$
Where the traffic flow rates are now functions of time.

$q_{od}$ is given for the eight incoming section of the network, and can be computed for the inner sections depending on the state of the traffic signal at $o$. The discrete-time rate of outgoing traffic $p_{od}^{k}$ can be given as 
$$
p_{od}^{k} = \begin{cases} \delta_{d}^{k} \beta_{od}v_{od}^{k}  &  \text{if } od \text{ is parallel to e-w}  \\
(1- \delta_{d}^{k})\beta_{od}v_{od}^{k},  &  \text{if } od \text{ is parallel to n-s} \end{cases}
$$
This can naturally be converted into a continuous-time formulation
$$
p_{od}(t) = \begin{cases} \delta_{d}(t) \beta_{od}v_{od}(t)  &  \text{if } od \text{ is parallel to e-w}  \\
(1- \delta_{d}(t))\beta_{od}v_{od}(t),  &  \text{if } od \text{ is parallel to n-s} \end{cases}
$$
Where we note that the controller $\delta$ is also now a function of time. The determination of parameter $\beta_{od}$ is left to simulation.

### Discrete-Time State Equation

We now consider the discrete-time state equation $V_{1}= \begin{bmatrix} v_{21}  & v_{31}  & v_{w1}  & v_{n1} \end{bmatrix}^{\top}$, representing traffic flow heading towards intersection $1$. Using the previous expressions of $p_{od}^{k}$ we get
$$\begin{align}\\
v^{k+1}_{21}&= v^{k}_{21}−\delta^{k}_{1}\beta_{21}v^{k}_{21}+\delta^{k}_{2}a_{2e}\beta_{e2}v^{k}_{e2}+(1−\delta^{k}_{2})(b_{2n}\beta_{42}v^{k}_{42} + b_{2s}\beta_{n2}v^{k}_{n2})\\
v^{k+1}_{31}&= v^{k}_{31}−\delta^{k}_{1}\beta_{31}v^{k}_{31}+\delta^{k}_{3}a_{3s}\beta_{s3}v^{k}_{s3}+(1−\delta^{k}_{3})(b_{3e}\beta_{43}v^{k}_{43} + b_{3w}\beta_{w3}v^{k}_{w3}) \\
v_{w1}^{k+1}&= v_{w1}^{k} - \delta_{1}^{k}\beta_{w1}v_{w1}^{k}+q_{w1} \\
v_{n1}^{k+1}&= v_{n1}^{k} - \left( 1- \delta_{1}^{k} \right) \beta_{n1} v_{n1}^{k} + q_{n1} 
\end{align}$$



