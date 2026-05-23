# Systems Modeling and Simulation Portfolio

This repository contains a collection of systems modeling and discrete-event simulation projects. Each project tackles a different business scenario using either the `simpy` framework or custom Python simulation logic to analyze operations, queues, and inventory.

## Projects Included

### 1. Cupcake Shop Inventory Optimization (`Cupcake_Inventory_Simulation.ipynb`)
An inventory management simulation using **SimPy**. 
* **Business Problem:** Balancing holding costs, ordering costs, and stockout penalties.
* **Approach:** Simulates daily operations with randomized demand (Gaussian distribution) and lead times. Tests various Reorder Points (`s`) against a Maximum Capacity (`S`) to find the optimal stock level that maximizes service level while minimizing total costs.

### 2. PlayStation Café Queuing System (`PS_Cafe_Queuing_Simulation.ipynb`)
An M/M/c queuing system simulation using **SimPy**.
* **Business Problem:** Evaluating the capacity of a gaming cafe with 3 rooms and a maximum waiting queue (buffer) of 10 customers.
* **Approach:** Uses non-stationary arrival rates (dynamic $\lambda$) to simulate rush hours and standard hours over multiple days. Calculates server utilization, drop rates (when the buffer is full), and plots queue lengths over time with warm-up analysis.

### 3. Multi-Server Queuing Simulation (`Multi_Server_Queue_Simulation.py`)
A custom discrete-event queuing simulation built from scratch in **Python**.
* **Business Problem:** Analyzing customer wait times and server idle times across a two-window service system.
* **Approach:** Allows for both manual data entry and random generation using weighted probabilities for interarrival and service times. Generates a tabular log of arrivals, service times, and queue status, followed by comprehensive system statistics (average wait, server utilization, probability of waiting).

## Prerequisites

To run these simulations, you will need Python installed along with the following libraries:
```bash
pip install simpy numpy matplotlib
