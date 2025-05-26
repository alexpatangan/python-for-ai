from ursina import *

app = Ursina()

# Plane
plane = Entity(model='cube', color=color.azure, scale=(1, 0.2, 2), collider='box')

# Camera
camera.parent = plane
camera.position = (0, 2, -5)
camera.rotation = (10, 0, 0)

# Ground
ground = Entity(model='plane', scale=(100, 1, 100), texture='white_cube', texture_scale=(100,100), collider='box')

def update():
    # Movement
    plane.rotation_y += held_keys['d'] * 100 * time.dt
    plane.rotation_y -= held_keys['a'] * 100 * time.dt
    plane.position += plane.forward * time.dt * 10
    plane.y += held_keys['w'] * time.dt * 5
    plane.y -= held_keys['s'] * time.dt * 5

app.run()


