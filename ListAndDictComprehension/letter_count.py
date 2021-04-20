sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

new_dict = {item:len(item) for item in  sentence.split()}

print(new_dict)