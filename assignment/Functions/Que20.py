''' Write a Python program that invokes a function after a specified period of time.
Sample Output: '''
import time

def delayed_function():
    print("This function is invoked after a specified period of time.")

def invoke_after_delay(seconds):
    print(f"Waiting for {seconds} seconds...")
    time.sleep(seconds)
    delayed_function()
delay_time = 5
invoke_after_delay(delay_time)
