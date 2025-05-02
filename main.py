import random 

def fcfs(requests, head):
    order = [head]
    total_movement = 0

    for req in requests:
        movement = abs(req - head)
        total_movement += movement
        head = req
        order.append(req)

    total_seek_time = total_movement
    return total_seek_time, order, total_movement


def scan_algorithm(requests, head, direction, disk_size):
    requests.sort()
    total_head_movement = 0
    seek_sequence = [head]

    if direction == "left":
        left = [r for r in requests if r < head]
        right = [r for r in requests if r >= head]
        
        left.reverse()
        for r in left:
            total_head_movement += abs(head - r)
            head = r
            seek_sequence.append(r)
             

        if right:
            if(left[-1] != 0):
                seek_sequence.append(0);
                total_head_movement += left[-1]
                
            total_head_movement += head  # move to 0
            head = 0
            for r in right:
                total_head_movement += abs(head - r)
                head = r
                seek_sequence.append(r)


    elif direction == "right":
        left = [r for r in requests if r < head]
        right = [r for r in requests if r >= head]

        for r in right:
            total_head_movement += abs(head - r)
            head = r
            seek_sequence.append(r)


        if left:
            if(right[-1] != disk_size - 1):
                seek_sequence.append(disk_size - 1)
                total_head_movement += (disk_size - 1) - right[-1] 
            
            total_head_movement += abs((disk_size - 1) - head)
            head = disk_size - 1
            left.reverse()
            for r in left:
                total_head_movement += abs(head - r)
                head = r
                seek_sequence.append(r)

    total_seek_time = total_head_movement

    return total_seek_time, seek_sequence, total_head_movement


def cscan(requests, head, disk_size):
    requests.sort()
    seek_sequence = [head]
    total_head_movement = 0

    # Separate requests into those greater and less than head
    left = [req for req in requests if req < head]
    right = [req for req in requests if req >= head]

    # Service requests to the right of head
    for req in right:
        total_head_movement += abs(head - req)
        head = req
        if (total_head_movement):
            seek_sequence.append(req)

    # Move head to the end of the disk (simulate circular jump to beginning)
    if left:
        total_head_movement += abs(head - (disk_size - 1))
        head = 0
        seek_sequence.append(199)
        seek_sequence.append(head)
        total_head_movement += abs((disk_size - 1) - head)

    # Service requests to the left
    for req in left:
        total_head_movement += abs(head - req)
        head = req
        seek_sequence.append(req)

    total_seek_time = total_head_movement

    return total_seek_time , seek_sequence, total_head_movement

def main():
    try:
        total_requests_possible = int(input("Enter the total number of possible requests (used for generating random request numbers): "))
        if total_requests_possible <= 0:
             print("Total number of possible requests must be a positive integer.")
             return

        initial_head_position = int(input("Enter the initial head position: "))

        num_cylinders = int(input("Enter the total number of cylinders (e.g., 200 for cylinders 0-199): "))
        if num_cylinders <= 0:
            print("Number of cylinders must be a positive integer.")
            return
        if initial_head_position < 0 or initial_head_position >= num_cylinders:
            print(f"Initial head position must be between 0 and {num_cylinders - 1}.")
            return

        print("\nAvailable Algorithms:")
        print("1. FCFS")
        print("2. SCAN")
        print("3. C-SCAN")
        algorithm_choice = input("Enter the number of the algorithm to use (1, 2, or 3): ")

        requests = [random.randint(0, num_cylinders - 1) for _ in range(total_requests_possible)]

        total_seek_time = 0
        execution_order = []
        total_head_movements = 0

        if algorithm_choice == '1':
            total_seek_time, execution_order, total_head_movements = fcfs(requests, initial_head_position)
            
        elif algorithm_choice == '2':
            scan_direction = input("Enter initial SCAN direction ('left' or 'right'): ").lower()
            
            if scan_direction not in ['left', 'right']:
                print("Invalid direction. Please enter 'left' or 'right'.")
                return
            
            total_seek_time, execution_order, total_head_movements = scan_algorithm(requests, initial_head_position, scan_direction, num_cylinders)
            
        elif algorithm_choice == '3':
            total_seek_time, execution_order, total_head_movements = cscan(requests, initial_head_position, num_cylinders)
            
        else:
            print("Invalid algorithm choice.")
            return


        print("\n--- Results ---")
        print(f"Generated Requests: {requests}")
        print(f"Execution Order: {' -> '.join(map(str, execution_order))}")
        print(f"Total Seek Time: {total_seek_time}")
        print(f"Total Head Movements: {total_head_movements}")
        print("---------------\n")

    except ValueError:
        print("Invalid input. Please enter integer values where required.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()