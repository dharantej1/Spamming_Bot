import time
import pyautogui
total_time=int(input("Enter The Total time to spam in seconds : "))
seq_times=[]

print("Initializing Spamming Process...")
time.sleep(10)
print("Started Spamming...")

while (True):
    start = time.time()
    #time.sleep(10)
    text = open('spamming_text.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
        time.sleep(1)
    time.sleep(6)
    end = time.time()

    print("Time for one complete spam :",end-start,"sec")
    seq_times.append(int(end-start))
    print("List of Times taken for the spam :",seq_times)

    if (sum(seq_times)>=total_time):
        print("Spam Completed Successfully!!!")
        break
