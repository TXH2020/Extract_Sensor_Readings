# Extract_Sensor_Readings

This is an app which sends the light sensor readings of an Android phone to a python application(receive_sensor_readings.py) to visualize the readings in the form of a real time graph. The transmission of readings occurs via a TCP Connection between the Android phone and the computer containing the Python Script. Add the IP address of your computer at the required location in the MainActivity.java file to make this app work. Note that this setup works only when both the sending and receiving devices are on the same network. In case of the devices being in different networks, add the public IP of your network. Make sure that the router has a port forwarding rule to route traffic from external networks to the receiving device.

I used a combination of these projects along with the knowledge of socket programming and android studio:

1. https://github.com/google-developer-training/android-advanced/tree/master/SensorListeners

2. https://www.geeksforgeeks.org/how-to-communicate-with-pc-using-android/

3. https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time
