class Process:
    def __init__(self, pid, btime, atime):
        self.pid = pid
        self.btime = btime
        self.atime = atime
        self.wtime = 0
        self.ttime = 0

def sjf_scheduling():
    print("\n SJF Scheduling...\n")
    n = int(input("Enter the number of processes: "))
    processes = []

    print("\nEnter the burst time and arrival time:")
    for i in range(n):
        btime = int(input(f"Process {i + 1} Burst Time: "))
        atime = int(input(f"Process {i + 1} Arrival Time: "))
        processes.append(Process(i + 1, btime, atime))

    processes.sort(key=lambda x: (x.atime, x.btime))

    current_process = None
    tbm = 0
    tot_ttime = 0

    print("\nProcess Scheduling:")
    print("\nSecond\tCurrent Process\tProcess Queue")

    while processes or current_process:
        for process in processes[:]:
            if process.atime <= tbm:
                print(f"\n{tbm}\t\t{process.pid if current_process else 'None'}\t\t{[p.pid for p in processes]}")
                if not current_process or process.btime < current_process.btime:
                    if current_process:
                        processes.append(current_process)
                    current_process = processes.pop(processes.index(process))
                    break

        if current_process:
            current_process.btime -= 1
            tbm += 1

            if current_process.btime == 0:
                current_process.ttime = tbm - current_process.atime
                tot_ttime += current_process.ttime
                current_process = None

    print(f"\nTotal Turnaround Time: {tot_ttime}")
    print(f"Average Turnaround Time: {tot_ttime / n}")

if __name__ == "__main__":
    sjf_scheduling()
