import numpy as np
from scipy.optimize import minimize

def principle_range(angle):
    while angle > np.pi:
        angle = angle - 2 * np.pi
    while angle < -np.pi:
        angle = angle + 2 * np.pi
    return angle

def heading_error(car_x, car_y, car_heading, prev_wp_x, prev_wp_y, next_wp_x, next_wp_y):
    path_dx = next_wp_x - prev_wp_x
    path_dy = next_wp_y - prev_wp_y
    path_angle = np.arctan2(path_dy, path_dx)
    
    error = car_heading - path_angle
    error = principle_range(error)
    return error

def lateral_error(car_x, car_y, prev_wp_x, prev_wp_y, next_wp_x, next_wp_y):
    numerator = abs((next_wp_y - prev_wp_y) * car_x - 
                    (next_wp_x - prev_wp_x) * car_y + 
                    next_wp_x * prev_wp_y - 
                    next_wp_y * prev_wp_x)
    
    dx = next_wp_x - prev_wp_x
    dy = next_wp_y - prev_wp_y
    denominator = np.sqrt(dx * dx + dy * dy)
    
    distance = numerator / denominator
    return distance

def velocity_error(current_velocity, desired_velocity):
    error = current_velocity - desired_velocity
    return error

def cost_function(car_x, car_y, car_heading, current_velocity, desired_velocity,
                  prev_wp_x, prev_wp_y, next_wp_x, next_wp_y,
                  weight_heading, weight_lateral, weight_velocity):
    
    error_heading = heading_error(car_x, car_y, car_heading, 
                                   prev_wp_x, prev_wp_y, next_wp_x, next_wp_y)
    error_lateral = lateral_error(car_x, car_y, 
                                   prev_wp_x, prev_wp_y, next_wp_x, next_wp_y)
    error_velocity = velocity_error(current_velocity, desired_velocity)
    
    error_heading_squared = error_heading * error_heading
    error_lateral_squared = error_lateral * error_lateral
    error_velocity_squared = error_velocity * error_velocity
    
    total_cost = (weight_heading * error_heading_squared + 
                  weight_lateral * error_lateral_squared + 
                  weight_velocity * error_velocity_squared)
    
    return total_cost, error_heading, error_lateral, error_velocity



def predict_next_state(car_x, car_y, car_heading, current_velocity, acceleration, yaw_rate, dt):
    next_velocity = current_velocity + acceleration * dt
    next_heading = car_heading + yaw_rate * dt
    next_x = car_x + next_velocity * np.cos(next_heading) * dt
    next_y = car_y + next_velocity * np.sin(next_heading) * dt
    
    return next_x, next_y, next_heading, next_velocity


def find_relevant_waypoints(car_x, car_y, waypoints):
    
    min_dist = float('inf')
    closest_idx = 0
    
    for i, (wx, wy) in enumerate(waypoints):
        dist = np.sqrt((car_x - wx)**2 + (car_y - wy)**2)
        if dist < min_dist:
            min_dist = dist
            closest_idx = i
    
    if closest_idx == 0:
        prev_idx = 0
        next_idx = 1
    else:
        prev_idx = closest_idx - 1
        next_idx = closest_idx
    
    if next_idx >= len(waypoints):
        next_idx = len(waypoints) - 1
    
    return waypoints[prev_idx], waypoints[next_idx]


car_x = 0.1
car_y = 3.1
car_heading = 0  
current_velocity = 5.5  
desired_velocity = 10.0  
acceleration = 1.3
yaw_rate = 0.23  


waypoints = [
    (1.0, 1.0),
    (0.9, 2.0),
    (0.9, 3.0),
    (1.0, 4.1),
    (1.7, 5.0),
    (2.3, 6.0)
]

weight_heading = 1.0
weight_lateral = 1.0
weight_velocity = 1.0

dt = 0.2  


print("Cost Function Analysis Over Time:")
print("")


states = []
costs = []

# Current state
current_x, current_y, current_heading, current_vel = car_x, car_y, car_heading, current_velocity

for timestep in range(4):  
    time = timestep * dt
    
 
    (prev_wp_x, prev_wp_y), (next_wp_x, next_wp_y) = find_relevant_waypoints(
        current_x, current_y, waypoints
    )
    
  
    total_cost, e_heading, e_lateral, e_velocity = cost_function(
        current_x, current_y, current_heading, current_vel, desired_velocity,
        prev_wp_x, prev_wp_y, next_wp_x, next_wp_y,
        weight_heading, weight_lateral, weight_velocity
    )
    

    states.append((current_x, current_y, current_heading, current_vel))
    costs.append((total_cost, e_heading, e_lateral, e_velocity))
    
    print(f"\nTimestamp t = {time:.1f}s:")
    print("-" * 60)
    print(f"Car Position:   ({current_x:.3f}, {current_y:.3f})")
    print(f"Car Heading:    {np.rad2deg(current_heading):.2f}°")
    print(f"Car Velocity:   {current_vel:.2f} m/s")
    print(f"Waypoints:      Prev({prev_wp_x}, {prev_wp_y}) → Next({next_wp_x}, {next_wp_y})")
    print()
    print(f"Heading Error:  {e_heading:.4f} rad ({np.rad2deg(e_heading):.2f}°)")
    print(f"Lateral Error:  {e_lateral:.4f} m")
    print(f"Velocity Error: {e_velocity:.4f} m/s")
    print(f"TOTAL COST:     {total_cost:.4f}")
    
 
    if timestep < 3:
        current_x, current_y, current_heading, current_vel = predict_next_state(
    current_x, current_y, current_heading, current_vel, acceleration, yaw_rate, dt


        )

print("\n" + "=" * 60)
print("\nSummary of Total Costs Over Time:")
print("-" * 60)
for i, (total_cost, _, _, _) in enumerate(costs):
    print(f"t = {i*dt:.1f}s: Cost = {total_cost:.4f}")



print("\n" + "=" * 60)
print("Optimzation using scipy library")
print("=" * 60)

def cost_to_minimize(x, *args):
    car_heading, car_velocity = x
    car_x, car_y, prev_wp_x, prev_wp_y, next_wp_x, next_wp_y, desired_velocity, weight_h, weight_l, weight_v, cost_func = args
    return cost_func(car_x, car_y, car_heading, car_velocity, desired_velocity, prev_wp_x, prev_wp_y, next_wp_x, next_wp_y, weight_h, weight_l, weight_v)[0]

print("\nOptimization of control variables over time:")

current_x, current_y, current_heading, current_vel = car_x, car_y, car_heading, current_velocity

for timestep in range(4):
    time = timestep * dt

  
    (prev_wp_x, prev_wp_y), (next_wp_x, next_wp_y) = find_relevant_waypoints(current_x, current_y, waypoints)

 
    x0 = [current_heading, current_vel]


    args = (current_x, current_y, prev_wp_x, prev_wp_y, next_wp_x, next_wp_y, 
            desired_velocity, weight_heading, weight_lateral, weight_velocity, cost_function)


    result = minimize(cost_to_minimize, x0, args=args, bounds=[(-np.pi, np.pi), (0, 10)])


    opt_heading, opt_velocity = result.x
    opt_cost = result.fun

    print(f"\nTimestamp t = {time:.1f}s:")
    print(f"  Optimal Heading:  {np.rad2deg(opt_heading):.2f}° ({opt_heading:.4f} rad)")
    print(f"  Optimal Velocity: {opt_velocity:.2f} m/s")
    print(f"  Minimum Cost:     {opt_cost:.4f}")

    if timestep < 3:
        current_x, current_y, current_heading, current_vel = predict_next_state(
            current_x, current_y, opt_heading, opt_velocity, acceleration, yaw_rate, dt
        )

