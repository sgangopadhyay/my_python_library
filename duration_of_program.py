### PROGRAM : Python Program to find out the exact time duration in which this program run.
### CREATED BY : Suman Gangopadhyay
### Date CREATED : 15-Nov-2017
import time
start_time = time.time()
for i in range(1,50):
    i = i+1
    time.sleep(1)
end_time = time.time()
print("The Duration for which this program run : %s Seconds" %(end_time-start_time))