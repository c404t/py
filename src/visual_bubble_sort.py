from time import sleep

RED = "\033[91m"
RESET = "\033[0m"

def print_colored(lst, moving_idx):
    output = []
    for i, val in enumerate(lst):
        if i == moving_idx:
            output.append(f"{RED}{val}{RESET}")
        else:
            output.append(str(val))
    print('[' + ', '.join(output) + ']', end='\r', flush=True)

def bubblesort(list):

   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            list[idx], list[idx+1] = list[idx+1], list[idx]
            sleep(0.8)
            #print(list, end='\r', flush=True)
            print_colored(list, idx+1)

list = [19,2,31,45,6,11,121,27]
print(list)
bubblesort(list)
print(list)
