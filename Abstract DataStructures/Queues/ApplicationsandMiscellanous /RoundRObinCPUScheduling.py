#PRACTICE PROBLEM Q03 — Round-Robin CPU Scheduling Simulation
def round_robin():

    from collections import deque as _deque

    def round_robin(processes, quantum):
        """processes: list of (pid, burst_time) tuples, in arrival order."""
        q = _deque(processes)
        time = 0
        completion = []
        while q:
            pid, remaining = q.popleft()
            if remaining <= quantum:
                time += remaining
                completion.append((pid, time))       # process finishes
            else:
                time += quantum
                remaining -= quantum
                q.append((pid, remaining))            # back of the queue
        return completion

    processes = [(1, 10), (2, 5), (3, 8)]   # (process id, burst time)
    quantum = 2
    print(f"Processes (id, burst): {processes}, quantum = {quantum}")
    result = round_robin(processes, quantum)
    print("Completion order (id, finish_time):", result)
    # Classic example: P2 finishes at t=15, P3 at t=21, P1 at t=23

round_robin()
