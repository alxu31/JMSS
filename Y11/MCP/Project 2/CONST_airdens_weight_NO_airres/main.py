import math
import sympy as sp

#! Changeable info
rpm = 394
passengers = 1 # 1-5
liftCoefficient = 0.12

#* Constants
g = 9.8
emptyMass = 730
airDensity = 1.225
bladeDiameter = 10.15

#* Calculated info
mass = emptyMass + (passengers*62)
referenceArea = math.pi*((bladeDiameter/2)**2)
velo = (rpm/60)*2*math.pi

weight = mass*g
lift = 1/2*(airDensity*(velo**2)*referenceArea*liftCoefficient)

t = sp.symbols('t')
#? Equations
acceleration = (lift-weight)/mass
velocity = sp.integrate(acceleration, t)
displacement = sp.integrate(velocity, t)

print(acceleration, velocity, displacement, sep='\n')

sp.plot_parametric(acceleration, velocity, (t, -0.5, 0.5), line_color='blue')



