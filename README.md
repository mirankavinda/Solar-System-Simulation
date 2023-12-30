# Solar System Simulation

A simple Python program using the Pygame library to simulate the motion of planets in the solar system. This program displays a scaled representation of the solar system, taking into account the positions, velocities, and gravitational interactions of celestial bodies. The simulation is based on real-world astronomical data and includes a selection of planets.

## Getting Started

To run this simulation, you'll need Python and the Pygame library installed on your computer. If you don't have Pygame installed, you can do so using pip:

```bash
pip install pygame
```
1. Clone this repository or download the `Solar-System-Simulation` file.

2. Run the program by executing `main.py`.

## How It Works

The program uses basic physics principles, including the law of universal gravitation, to simulate the motion of planets in our solar system. It considers the gravitational forces between the planets and the sun. Each planet's position and velocity are updated at regular time intervals to create a real-time simulation.

## Features

- Realistic representation of the solar system with scaled positions and sizes.
- Gravitational forces between planets and the sun.
- Smooth animation using Pygame.
- Planetary information displayed, including distance from the sun (in kilometers).

## Planets

The simulation includes the following planets:

- Sun: The center of the solar system.
- Earth: Represented in blue.
- Mars: Represented in red.
- Mercury: Represented in dark grey.
- Venus: Represented in white.

## Adding More Planets

- Jupiter: Represented in a brownish color.
- Saturn: Represented in a pale yellow color.
- Uranus: Represented in light blue.
- Neptune: Represented in dark blue.

jupiter = Planet(5.203 * Planet.AU, 0, 25, (227, 163, 49), 1.898 * 10**27)
jupiter.y_vel = -13.06 * 1000

saturn = Planet(9.537 * Planet.AU, 0, 20, (210, 180, 140), 5.683 * 10**26)
saturn.y_vel = -9.68 * 1000

uranus = Planet(19.22 * Planet.AU, 0, 18, (173, 216, 230), 8.681 * 10**25)
uranus.y_vel = -6.80 * 1000

neptune = Planet(30.05 * Planet.AU, 0, 18, (0, 0, 128), 1.024 * 10**26)
neptune.y_vel = -5.43 * 1000

planets = [sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]


To add more planets to the simulation, you can use the Planet class with the provided data. Simply create a new instance of the Planet class and add it to the planets list. Be aware that adding many planets may require adjustments to the screen size or other parameters to ensure everything fits within the window

For example, you can add additional planets like this:

Example of adding more planets
Replace these values with the parameters for your desired planets
- `new_planet = Planet(x_position, y_position, radius, color, mass)`
- `new_planet.y_vel = orbital_velocity`
- `planets.append(new_planet)`

This simulation simplifies many aspects of the solar system and does not consider all gravitational interactions, orbital eccentricities, or physical properties of planets. It provides a basic, visually pleasing representation of planetary motion.
  
