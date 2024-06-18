def priority_scheduling(processes, priorities):
  """Schedules processes in priority order.

    processes: A list of processes.
    priorities: A list of priorities, where the ith element is the priority of the ith process.
  Returns:
    A list of processes, scheduled in priority order.
  """

  sorted_processes = sorted(zip(processes, priorities), key=lambda x: x[1])
  return [process for process, _ in sorted_processes]


if __name__ == "__main__":
  processes = ["P1", "P2", "P3", "P4"]
  priorities = [1, 2, 3, 4]

  scheduled_processes = priority_scheduling(processes, priorities)
  print("Scheduled processes:", scheduled_processes)