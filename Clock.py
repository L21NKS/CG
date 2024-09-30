import matplotlib.pyplot as plt
import numpy as np

def bresenham_circle(radius):
    x = 0
    y = radius
    d = 3 - 2 * radius
    points = []

    def draw_circle_points(x, y):
        points.extend([
            (x, y), (-x, y), (x, -y), (-x, -y),
            (y, x), (-y, x), (y, -x), (-y, -x)
        ])

    while x <= y:
        draw_circle_points(x, y)
        if d <= 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

def plot_circle_with_ticks(radius, num_ticks, hour, minute):
    points = bresenham_circle(radius)
    
    unique_points = list(set(points))
    unique_points.sort(key=lambda p: np.arctan2(p[1], p[0]))

    unique_points.append(unique_points[0])
    
    x_coords = [point[0] for point in unique_points]
    y_coords = [point[1] for point in unique_points]

    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords, color='blue')

    tick_length = 0.1 * radius
    for i in range(num_ticks):
        angle = 2 * np.pi * i / num_ticks
        x_tick_start = (radius - tick_length) * np.cos(angle)
        y_tick_start = (radius - tick_length) * np.sin(angle)
        x_tick_end = radius * np.cos(angle)
        y_tick_end = radius * np.sin(angle)
        
        ax.plot([x_tick_start, x_tick_end], [y_tick_start, y_tick_end], color='red', lw=1.5)

    minute_angle = np.deg2rad(360 - minute * 6 + 90)  
    hour_angle = np.deg2rad(360 - ((hour % 12) * 30 + minute * 0.5) + 90)  

    ax.arrow(0, 0, 0.5 * radius * np.cos(hour_angle),
             0.5 * radius * np.sin(hour_angle), 
            head_width=0.05 * radius, head_length=0.1 * radius, fc='green', ec='green')

    ax.arrow(0, 0, 0.8 * radius * np.cos(minute_angle),
             0.8 * radius * np.sin(minute_angle), 
            head_width=0.05 * radius, head_length=0.1 * radius, fc='blue', ec='blue')

    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f'Bresenham Circle with radius {radius} and {num_ticks} ticks')
    ax.grid(True)
    plt.show()

# Ввод данных от пользователя
radius = int(input("Введите радиус циферблата: "))
num_ticks = 12
hour = int(input("Часы (0-23): "))
minute = int(input("Минуты (0-59): "))

# Отображение часов
plot_circle_with_ticks(radius, num_ticks, hour, minute)

