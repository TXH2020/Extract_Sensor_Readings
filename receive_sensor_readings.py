import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
port = 4444
s = socket.socket()
s.bind(('', port))
s.listen(5)


def get_sensor_value(s):
    c, addr = s.accept()
    string=str(c.recv(10000))
    data=0.0
    try:
        data=float(string[16:len(string)-2])
    except:
        pass
    return data

def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    temp_c = get_sensor_value(s)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Light Sensor Reading')
    plt.ylabel('Light Intensity')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=0)
plt.show()


