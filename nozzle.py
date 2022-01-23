# TODO: visualisation
import math

print("-----------------------DIVERGENCE----------------------------")
# diamater of throat
dt = 5
# expansion ratio
exp = 4.84
# div angle
div = 30
div_half = div / 2
div_rad = div_half / 180.0 * math.pi
print("Init conditions  ", "throat: ", dt, "expansion: ", exp, "divergence:", div)

at = math.pi*(dt/2)**2
ae = at*exp
re = math.sqrt(ae/math.pi)
print("Exit radius:", re)
print("Exit diameter:", re*2)
print("Divergence half radians:", div_rad, "Tanges:", math.tan(div_rad))
# calculations on divergance trapezoid
div_len = (re - (dt/2)) / math.tan(div_rad)
print("Divergence length:", div_len)



# -------------------------------- convergence ------------------
print("-----------------------CONV----------------------------")
conv_deg = 30
conv_rad = conv_deg/180.0 * math.pi
tan_conv = math.tan(conv_rad)

chamber_d = 18
chamber_r = chamber_d/2
chamber_r_trapezoid = 9 - dt/2
chamber_len = chamber_r_trapezoid / tan_conv
print("Convergence length:", chamber_len)


# ----- expansion ration calc -----
# http://www.nakka-rocketry.net/articles/noz_example3.pdf
# KNSU: https://www.nakka-rocketry.net/succhem.html
print("-----------------------TODO EXPANSION RATIO--------------------------")
k = 1.044
pe = 1.0
p0 = 21.43 # how this is calculated???
print("Convergence", "k:", k, "p0:", p0)

fst = ((k + 1)/2.0)**(1.0/(k-1))
print("First term:", fst)
sec = (pe / p0)**(1.0/k)
print("Sec term:", sec)
third = (k + 1)/(k - 1.0)*(1.0 - (pe / p0)**((k-1)/k))
print("Third term: ", third)
expX = fst*sec*math.sqrt(third)
ratio = 1.0 / expX
print("Expansion ratio: ", ratio)

aX = at*ratio
rX = math.sqrt(aX/math.pi)
print("Radius X: ", rX)
print("Diameter X:", rX*2)
