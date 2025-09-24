from vpython import *
#Web VPython 3.2

#Set up variables
#universal gravitational constant 
G = 6.67e-11

#end time(3 years in seconds)
endTime = 365 * 24 * 60 * 60 * 2000

#mass of the star1 and star2 (kg)
mStar1 = 2e24
mStar2 = 1e24



# radius of the star1 and star2 (m)

Rstar1 = 6.957e9
Rstar2 = 6.3781e9

#starting value of r (1AU in m)
r0 = 1.5e11

#orbital velocity of star2 (m/s)
vStar2 = 1e1

# constant for radiative force 
µ = 4e29

#set up Star1
Star1 = sphere(pos = vec(-1.1e11,0,0), radius = Rstar1, color = color.red, make_trail = True)
#set up Star2
Star2 = sphere(pos = vec(1.5e11,0,0), radius = Rstar2, color = color.blue, make_trail = True)




#set up momentum
Star2.v = vec(0,1e1,0)
Star2.p = mStar2 * Star2.v 

#set up momentum
Star1.v = vec(0,0,0)
Star1.p = -Star2.p


# Measure initial kinetic energy
Star1.KE0 = (Star1.p.mag2) / (2 * mStar1)
Star2.KE0 = (Star2.p.mag2) / (2 * mStar2)

 
# Initialize work 
Star1.work = 0
Star2.work = 0


    # plot work vs. time (J)
WORKGraph = graph(title="Work on System Over Time (J/s)", xtitle="Time (s)", ytitle="Work (J)")
workStar1Curve = gcurve(graph= WORKGraph, color=color.red)
workStar2Curve = gcurve(graph= WORKGraph, color=color.blue)

    # plot change in KE vs time (J)
KEGraph = graph(title="Change in Kinetic Energy Over Time (J/s)", xtitle="Time (s)", ytitle="Kinetic Energy (J)")
keStar1Curve = gcurve(graph= KEGraph, color=color.red)
keStar2Curve = gcurve(graph= KEGraph, color=color.blue)

    # change in PE (U) vs.time (J)
PEGraph = graph(title="Change in Potential Energy Over Time (J/s)", xtitle="Time (s)", ytitle="Potential Energy (J)")
peStar1Curve = gcurve(graph= PEGraph, color=color.red)
peStar2Curve = gcurve(graph= PEGraph, color=color.blue)

    # total mechanical energy vs time (J)
MEGraph = graph(title="Total Mechanical Energy Over Time (J/s)", xtitle="Time (s)", ytitle="Total Mechanical Energy (J)")
meStar1Curve = gcurve(graph= MEGraph, color=color.red)
meStar2Curve = gcurve(graph= MEGraph, color=color.blue)

### with sep ###

    # work over separation (dist from star 1 and star 2)
WORKsepGraph = graph(title = "Work Over Separation (J/m)", xtitle = "Separation (m)", ytitle = "Change in Kinetic Energy (J)")
workStar1sepCurve = gcurve(graph = WORKsepGraph, color = color.red)
workStar2sepCurve = gcurve(graph = WORKsepGraph, color = color.blue)


    # change in KE over separation
KEsepGraph = graph(title = "Change in Kinetic Energy Over Separation (J/m)", xtitle = "Separation (m)", ytitle = "Change in Kinetic Energy (J)")
keStar1sepCurve = gcurve(graph = KEsepGraph, color = color.red)
keStar2sepCurve = gcurve(graph = KEsepGraph, color = color.blue)


    # change in PE over separation
PEsepGraph = graph(title = "Change in Potential Energy Over Separation (J/m)", xtitle = "Separation (m)", ytitle = "Change in Potential Energy (J)")
peStar1sepCurve = gcurve(graph = PEsepGraph, color = color.red)
peStar2sepCurve = gcurve(graph = PEsepGraph, color = color.blue)


    # total ME over separation
MECHsepGraph = graph(title = "Total Mechanical Energy Over Separation (J/m)", xtitle = "Separation (m)", ytitle = "Total Mechanical Energy (J)")
meStar1sepCurve = gcurve(graph = MECHsepGraph, color = color.red)
meStar2sepCurve = gcurve(graph = MECHsepGraph, color = color.blue)


#current time
t = 0
#time step changed
dt = 24 * 60 * 60 * 30

r = Star1.pos - Star2.pos


# initial PE
Star1.PE0 = - ((G * mStar2 * mStar1) / r.mag)  
Star2.PE0 = - ((G * mStar2 * mStar1) / r.mag)


while t < endTime:
    #animation rate changed
    rate(2000)
    
    #define r between star2 and star1
    r = Star1.pos - Star2.pos   
    
    #Calc force applied on star1 by star2
    forceStar1 = ((G * mStar2 * mStar1) / r.mag2) * (-r.hat)
    #Calc force applied on star2 by star1
    forceStar2 = ((G * mStar2 * mStar1) / r.mag2) * (r.hat)
    
    
    # calculate KE  
    Star1.KE = (Star1.p.mag2) / (2 * mStar1)
    Star2.KE = (Star2.p.mag2) / (2 * mStar2)
    
    #calculating PE 
    Star1.PE = - ((G * mStar2 * mStar1) / r.mag)
    Star2.PE = - ((G * mStar2 * mStar1) / r.mag)
    
        
    # update work which is PE + KE * displacement  
    Star1.work += forceStar1.dot(Star1.v * dt)
    Star2.work += forceStar2.dot(Star2.v * dt)
    
    #change in KE
    Star1.deltaKE = Star1.KE - Star1.KE0
    Star2.deltaKE = Star2.KE - Star2.KE0
      
    #change in PE 
    Star1.deltaPE = Star1.PE - Star1.PE0
    Star2.deltaPE = Star2.PE - Star2.PE0 
    
    #total mechanical energy
    totalMECH1 = Star1.KE +  Star1.PE 
    totalMECH2 = Star2.KE + Star2.PE

    #update momentum for each body using force
    Star1.p = Star1.p + (forceStar1 * dt)
    Star2.p = Star2.p + (forceStar2 * dt)
    
    #calc velocity from updated momentum
    Star1.v = Star1.p / mStar1
    Star2.v = Star2.p / mStar2

    
    #update position using velocity
    Star1.pos = Star1.pos + (Star1.v * dt)
    Star2.pos = Star2.pos + (Star2.v * dt)
    
    
    #Update Time
    t = t + dt
    
    # plot work vs. time (J)
    workStar1Curve.plot(pos=(t, Star1.work))
    workStar2Curve.plot(pos=(t, Star2.work))
    
    # plot chnage in KE vs time (J)
    keStar1Curve.plot(pos=(t, Star1.KE))
    keStar2Curve.plot(pos=(t, Star2.KE))
    
    # change in PE (U) vs.time (J)
    peStar1Curve.plot(pos=(t, Star1.PE))
    peStar2Curve.plot(pos=(t, Star2.PE))
    
    # total mechanical energy vs time (J)
    meStar1Curve.plot(pos=(t, totalMECH1))
    meStar2Curve.plot(pos=(t, totalMECH2))
    
    # FOR OUTPUT
    
    
### with sep ###
    

    workStar1sepCurve.plot(pos=(r.mag, Star1.work))
    workStar2sepCurve.plot(pos=(r.mag, Star2.work))
    
 
    keStar1sepCurve.plot(pos=(r.mag, Star1.KE))
    keStar2sepCurve.plot(pos=(r.mag, Star2.KE))
    

    peStar1sepCurve.plot(pos=(r.mag, Star1.PE))
    peStar2sepCurve.plot(pos=(r.mag, Star2.PE))
    

    meStar1sepCurve.plot(pos=(r.mag, totalMECH1))
    meStar2sepCurve.plot(pos=(r.mag, totalMECH2))
