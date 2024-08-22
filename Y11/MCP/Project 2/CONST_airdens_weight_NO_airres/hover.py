import math

#! Changeable info
passengers = 1 # 1-5
liftCoefficient = 0.12

#* Info
emptyMass = 730
airDensity = 1.225
bladeDiameter = 10.15
mass = emptyMass + (passengers*62)
g = 9.8
referenceArea = math.pi*((bladeDiameter/2)**2)

velo = math.sqrt((2*mass*g)/(airDensity*referenceArea*liftCoefficient))

rpm = (velo*60)/(2*math.pi)
print(velo)
print(rpm)