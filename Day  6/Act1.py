import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title('Elastic Ball Drop and Bounce', fontsize=16)
ax.set_facecolor('skyblue')

# Ball properties
ball_radius = 0.5
ball_color = 'red'
ball = plt.Circle((5, 9), ball_radius, fc=ball_color)

# Add the ball to the axis
ax.add_patch(ball)

# Parameters for the animation
gravity = 9.8  # acceleration due to gravity
bounce_coefficient = 0.75  # energy loss factor on each bounce
dt = 0.05  # time interval between frames

# Initial conditions
y_pos = 9
y_velocity = 0

# Function to update the position of the ball
def update(frame):
    global y_pos, y_velocity

    # Update the position and velocity
    y_velocity -= gravity * dt
    y_pos += y_velocity * dt

    # Check for collision with the ground
    if y_pos - ball_radius < 0:
        y_pos = ball_radius
        y_velocity = -y_velocity * bounce_coefficient

    # Update the position of the ball
    ball.set_center((5, y_pos))
    return ball,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=dt * 1000, blit=True)

# Display the animation
plt.show()
