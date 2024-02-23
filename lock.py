#Ankush Singla
#sit210
#Door lock/Unlock Code
import RPi.GPIO as GPIO
import tkinter as tk

# Define the GPIO pin connected to the relay module
relay_pin = 17  # Change this to the actual pin you have connected to the relay

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Function to toggle the lock state and update the status label
def toggle_lock():
    global is_locked
    is_locked = not is_locked
    update_button_text()

    if is_locked:
        status_label.config(text="Locking...", fg="green", font=("Arial", 24))
        GPIO.output(relay_pin, GPIO.HIGH)
        window.after(1000, lock_done)
    else:
        status_label.config(text="Unlocking...", fg="red", font=("Arial", 24))
        GPIO.output(relay_pin, GPIO.LOW)
        window.after(1000, unlock_done)

# Function to update the button text
def update_button_text():
    lock_button.config(text="Unlock" if is_locked else "Lock", font=("Arial", 20), bg="blue" if is_locked else "green")

# Function to display "Locking Done"
def lock_done():
    status_label.config(text="Locking Done", fg="green", font=("Arial", 24))

# Function to display "Unlocking Done"
def unlock_done():
    status_label.config(text="Unlocking Done", fg="red", font=("Arial", 24))

# Create a GUI window
window = tk.Tk()
window.title("Smart Door Lock Control")

# Configure style
window.configure(bg="white")

# Create a frame to center the elements
frame = tk.Frame(window, bg="white")
frame.pack(expand=True)

# Create a large button to lock/unlock the door
lock_button = tk.Button(frame, text="Lock", command=toggle_lock, width=15, height=3, bg="green", fg="white", font=("Arial", 20))
lock_button.pack(padx=20, pady=20)

# Create a label to display the status
status_label = tk.Label(frame, text="Door is unlocked", font=("Arial", 24), bg="white")
status_label.pack(padx=10, pady=10)

is_locked = False
update_button_text()

try:
    window.geometry("800x600")  # Set window size for larger resolution
    window.mainloop()

except KeyboardInterrupt:
    print("Exiting the control script.")
    GPIO.cleanup()
