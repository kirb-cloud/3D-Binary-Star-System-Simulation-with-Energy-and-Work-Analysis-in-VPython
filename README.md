# 3D-Binary-Star-System-Simulation-with-Energy-and-Work-Analysis-in-VPython
This simulation models the motion of a binary star system using Newtonian mechanics in 3D space with VPython. It tracks the position, velocity, momentum, kinetic energy, potential energy, work, and total mechanical energy of two interacting stars over time.

## Features
- 3D visualization of two stars with **trails** representing motion.
- Real-time calculations of:
  - **Momentum** (`p = m * v`)
  - **Velocity** (`v = p / m`)
  - **Kinetic Energy** (`KE = |p|^2 / 2m`)
  - **Potential Energy** (`PE = - G m1 m2 / r`)
  - **Work Done** (`W = Σ F · v dt`)
  - **Total Mechanical Energy** (`ME = KE + PE`)
- Interactive graphs:
  - Work vs Time
  - Kinetic Energy vs Time
  - Potential Energy vs Time
  - Total Mechanical Energy vs Time
  - Work, KE, PE, ME vs Separation distance

## Equations Used

**Gravitational Force:**  
`F = G * m1 * m2 / r^2`  

**Momentum:**  
`p = m * v`  

**Velocity from Momentum:**  
`v = p / m`  

**Kinetic Energy (KE):**  
`KE = |p|^2 / (2 * m)`  

**Gravitational Potential Energy (PE):**  
`PE = - G * m1 * m2 / r`  

**Work Done:**  
`W = Σ F · (v * dt)`  

**Total Mechanical Energy (ME):**  
`ME = KE + PE`  

## Simulation Setup

- **Stars:**
  - Star 1: mass = `2e24 kg`, radius = `6.957e9 m`
  - Star 2: mass = `1e24 kg`, radius = `6.3781e9 m`
- **Initial positions:**  
  - Star1: `(-1.1e11, 0, 0)`  
  - Star2: `(1.5e11, 0, 0)`
- **Initial velocities:**  
  - Star2: `10 m/s` perpendicular to the separation vector  
  - Star1: velocity set to conserve total momentum
- **Time step:** `dt = 24*60*60*30` seconds (~1 month)
- **Simulation duration:** `2000 years` (in seconds)

## How It Works

1. **Initialization**
   - Define constants (G, star masses, radii, initial separation, velocities).
   - Create VPython `sphere` objects for the stars with trails.
   - Initialize momentum, velocity, kinetic energy, and work.

2. **Time Evolution (Loop)**
   - Update the **separation vector** `r`.
   - Compute the **gravitational force** on each star.
   - Update **momentum**: `p = p + F * dt`
   - Calculate **velocity**: `v = p / m`
   - Update **position**: `r = r + v * dt`
   - Compute **KE** and **PE**
   - Update **work**: `W += F · (v * dt)`
   - Calculate **total mechanical energy**: `ME = KE + PE`

3. **Graph Updates**
   - Plot **Work, KE, PE, ME** vs **time**
   - Plot the same quantities vs **separation distance**

4. **Iteration**
   - Continue until the simulation end time is reached
   - All graphs and star positions are continuously updated

## Graphs

- Work vs Time  
- Kinetic Energy vs Time  
- Potential Energy vs Time  
- Total Mechanical Energy vs Time  
- Work vs Separation  
- Kinetic Energy vs Separation  
- Potential Energy vs Separation  
- Total Mechanical Energy vs Separation
