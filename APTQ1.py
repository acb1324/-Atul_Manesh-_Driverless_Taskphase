import numpy as np

x=10
y=5
heading=30
v=5
acc=1
yawrate_deg=10
time=0.2

degree_rad = np.deg2rad(heading)
yawrate_rad = np.deg2rad(yawrate_deg)

new_heading = degree_rad + yawrate_rad * time

new_x = x + v * np.cos(new_heading) * time
new_y = y + v * np.sin(new_heading) * time
new_v = v + acc * time

dx = new_v * np.cos(new_heading) * time
dy = new_v * np.sin(new_heading) * time

new_x = x + dx
new_y = y + dy

B1 = np.array([12, 7])
B2 = np.array([8, 6])
Y1 = np.array([13, 4])
Y2 = np.array([9, 3])
cones_global = np.array([B1, B2, Y1, Y2])

def global_to_car_frame(car_x, car_y, car_theta, points):
    translated_points = points - np.array([car_x, car_y])
    c, s = np.cos(-car_theta), np.sin(-car_theta)
    R = np.array([[c, -s],
                  [s, c]])  
    return translated_points.dot(R.T)
cones_in_car_initial = global_to_car_frame(x, y, np.deg2rad(heading), cones_global)
cones_in_car_new = global_to_car_frame(new_x, new_y, new_heading, cones_global)

print("")
print("")

print("New X Coordinate : ", new_x)
print("")
print("New Y Coordinate : ", new_y)
print("")
print("")
print("New Heading : ", np.rad2deg(new_heading) ," degrees")
print("")
print("")
print("Initial position of cones in Car Frame : \n" , *cones_in_car_initial, sep="\n")
print("")
print("Updated position in Car Frame : \n", *cones_in_car_new, sep="\n")
