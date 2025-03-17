charge = int(input("Enter the parking charges : "))

entry_time = int(input("Enter the hours for the start time of parking : "))
exit_time = int(input("Enter the hours of the exit time  of the parking :"))
time = entry_time - exit_time
automated_system = charge * time

fee = lambda fee:automated_system+time
print(f"Total parking fee {fee}")

