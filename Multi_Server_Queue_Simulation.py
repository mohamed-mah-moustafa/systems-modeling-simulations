import random

interarrival_times = [1, 2, 3, 4]
service_times = [3,4,5]
weightsA = [0.3, 0.4, 0.2, 0.1]
weightsB = [0.5, 0.3, 0.2]
results = {
    "ID": [],
    "Interarrival": [],
    "Arrival": [],
    "Window": [],
    "Service Start": [],
    "Service end": [],
    "wait time":[],
    "no in queue 1": [],
    "no in queue 2": [],
    "idle 1": [],
    "idle 2": [],
    "sys time": []
}

arrival_time = 0 
w1_free_at = 0
w2_free_at = 0

# 1. Ask the user for the mode
mode = input("Select Mode (1: Manual, 2: Random): ")

if mode == "1":
    # Manually
    manual_iat = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    manual_serv = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
else:
    # We will generate the numbers inside the loop
    pass

for i in range(1, 11):
    
    if mode == "1":
        iat = manual_iat[i-1]
        serv = manual_serv[i-1]
    else:
        iat = random.choices(interarrival_times, weights=weightsA)[0]
        serv = random.choices(service_times, weights=weightsB)[0]
    # 2. Update Clock
    if i == 1:
        iat = 0  # The first person has no 'time between'
        arrival_time = 0
    else:
        arrival_time += iat
    waittime = 0
    idle_1 = 0
    idle_2 = 0
    
    # 3. Window Assignment Logic
    if arrival_time >= w1_free_at:
        # Window 1 is free
        assigned_window = 1
        idle_1 = arrival_time - w1_free_at
        service_start = arrival_time
    elif arrival_time >= w2_free_at:
        # Window 2 is free
        assigned_window = 2
        idle_2 = arrival_time - w2_free_at
        service_start = arrival_time
    else:
        # Both Busy...then Pick the one that finishes first
        if w1_free_at <= w2_free_at:
            assigned_window = 1
            service_start = w1_free_at
        else:
            assigned_window = 2
            service_start = w2_free_at
        
        waittime = service_start - arrival_time

    service_end = service_start + serv
    
    # 4. UPDATE WINDOW FREE TIME
    if assigned_window == 1:
        w1_free_at = service_end
    else:
        w2_free_at = service_end
        
        
    q1 = 0
    q2 = 0      
    for j in range(len(results["ID"])):
        # A person is in the QUEUE only if their service starts AFTER this arrival
        # If Service Start <= arrival_time, they are already being served
        if results["Window"][j] == 1 and results["Service Start"][j] > arrival_time:
            q1 += 1
        if results["Window"][j] == 2 and results["Service Start"][j] > arrival_time:
            q2 += 1


    results["no in queue 1"].append(q1)
    results["no in queue 2"].append(q2)
    results["Arrival"].append(arrival_time)
    results["ID"].append(i)
    results["idle 1"].append(idle_1)
    results["idle 2"].append(idle_2)
    results["Interarrival"].append(iat)
    results["Service end"].append(service_end)
    results["Service Start"].append(service_start)
    results["sys time"].append(service_end-arrival_time)
    results["Window"].append(assigned_window)
    results["wait time"].append(waittime)

# 1. Print the Headers
headers = list(results.keys())
header_string = " | ".join([f"{h:<10}" for h in headers])
print(header_string)
print("-" * (len(header_string)-1))

# 2. Print the Data
# We assume all lists are the same length
num_rows = len(results[headers[0]]) 

for i in range(num_rows):
    row = [f"{results[h][i]:<11}" for h in headers]
    print(" | ".join(row))

#calculate the stats
waiting_customers = [w for w in results["wait time"] if w > 0]
num_who_waited = len(waiting_customers)

avgt_in_sys=sum(results["sys time"])/10
avgQlen=(sum(results["no in queue 1"])+sum(results["no in queue 2"]))/20
untilization=sum(results["sys time"])/(service_end*2)
avgWait=sum(results["wait time"])/10
probWait=num_who_waited/10
probIdle=(sum(results["idle 1"]) + sum(results["idle 2"]))/(service_end*2)
avgIat=sum(results["Interarrival"])/10
if num_who_waited > 0:
    avg_wait_for_waiters = sum(waiting_customers) / num_who_waited
else:
    avg_wait_for_waiters = 0
    
#print the stats    
print("\n" + "="*30)
print("   SIMULATION STATISTICS")
print("="*30)
print(f"1. Avg time in system:              {avgt_in_sys:.2f} min")
print(f"2. Average queue length:            {avgQlen:.2f} customers")
print(f"3. Server utilization:               {untilization:.2%}")
print(f"4. Average waiting time:            {avgWait:.2f} min")
print(f"5. Probability of waiting:          {probWait:.2%}")
print(f"6. Probability of server idle:      {probIdle:.2%}")
print(f"7. Average time between arrivals:   {avgIat:.2f} min")
print(f"8. Avg wait time (for those who wait): {avg_wait_for_waiters:.2f} min")
print("="*30)