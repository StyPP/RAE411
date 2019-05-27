#import
import matplotlib.pyplot as plt

#create empty lists and end
time = []
end = 20
nbtimes = 4

#Read data and append to lists
file = open("timeserver", "r")
for i in range(end):
    line = file.readline().rstrip()
    line = float(line)
    time.append(line)

for j in range(nbtimes - 1):
    for i in range(end):
        line = file.readline().rstrip()
        line = float(line)
        time[i] = time[i] + line
        
for i in range(end):
    time[i] = time[i] / nbtimes
    
file.close()

#graphics settings
plt.xlim(0, end)
plt.ylim(0, 1)

plt.grid(b=None, axis='both', linestyle = '--')
plt.title("Copy Project")
plt.xlabel("Size (in Mo)")
plt.ylabel("Time")

fig = plt.gcf()
fig.set_size_inches(17.5, 8.5)

x = [i for i in range(0, end)]

#-------------------------------------------------------------------------------

plt.plot(x, time, color="red")

plt.savefig('graphnetwork.pdf')
plt.savefig('graphnetwork.png')
