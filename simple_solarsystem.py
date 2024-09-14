from solarsystem import Solar_system, Sun, Planet

solar_system = Solar_system(width=1800, height=1400)

sun = Sun(solar_system, mass=10_000)
planets = (
    Planet(
        solar_system,
        mass=1,
        position=(-350, 0),
        velocity=(0.2, 0.4),
    ),
    Planet(
        solar_system,
        mass=2,
        position=(-270, 0),
        velocity=(0, 0.6),
    ),
    Planet(
        solar_system,
        mass=2.4,
        position=(-200, 20),
        velocity=(0, 0.6),
    ),
    Planet(
        solar_system,
        mass=1,
        position=(-300, 0),
        velocity=(0.2, 0.4),
    ),
    Planet(
        solar_system,
        mass=1,
        position=(-400, 0),
        velocity=(0.2, 0.4),
    ),
)
while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()