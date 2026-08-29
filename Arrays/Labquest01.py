#4) Production Line Optimization:  
#A factory's production system stores the sequence of jobs assigned to a production line in an array jobs.
#Each non-zero value represents an active production job, while 0 represents an idle or empty slot. 
#Before starting production, the system must reorganize the schedule so that all idle slots are moved to the end,
#while maintaining the original order of all active jobs. 
#Write a function reorganize_jobs(jobs) to perform this operation without creating a new array.  
#Input: jobs = [101, 102, 0, 103, 104]  
#Output: [101, 102, 103, 104, 0]


def reorganize_jobs(jobs):
    write_pos = 0
    # Pass 1: shift every active (non-zero) job forward, preserving order
    for read_pos in range(len(jobs)):
        if jobs[read_pos] != 0:
            jobs[write_pos] = jobs[read_pos]
            write_pos += 1
 
    # Pass 2: fill the remaining tail with idle slots (0)
    for i in range(write_pos, len(jobs)):
        jobs[i] = 0
 
    return jobs
 
 
def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)
 
 
def run_case(jobs, label):
    original = jobs.copy()
    result = reorganize_jobs(jobs)
    print(f"{label}")
    print(f"  Input:  {original}")
    print(f"  Output: {result}")
 
 
if __name__ == "__main__":
    section("Problem 4 — Production Line Optimization")
 
    # Given example
    run_case([101, 102, 0, 103, 104], "Example from problem statement")
    # Expected: [101, 102, 103, 104, 0]
 
    # Additional test cases (edge cases worth checking on any array problem)
    run_case([0, 0, 101, 0, 102, 0, 103], "Idle slots scattered, including leading zeros")
    run_case([0, 0, 0], "All idle — no active jobs at all")
    run_case([101, 102, 103], "No idle slots — already fully packed")
    run_case([], "Empty production line")
    run_case([0], "Single idle slot")
    run_case([101], "Single active job")
 
