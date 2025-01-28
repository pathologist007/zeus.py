import shutil
import os
import psutil  # Use 'pip install psutil' if not installed

def find_usb_drive():
    # Iterate through all disk partitions
    for partition in psutil.disk_partitions():
        if "removable" in partition.opts:  # Check if the drive is removable (USB)
            return partition.mountpoint
    return None  # Return None if no USB drive is found

def copy_self_to_usb(num_copies):
    # Get the current script's path
    script_path = os.path.abspath(__file__)

    # Find the USB drive path
    usb_path = find_usb_drive()

    if usb_path:
        for i in range(num_copies):
            # Construct the destination file path
            destination_path = os.path.join(usb_path, f"script_copy_{i + 1}.py")
            
            # Copy the script to the USB drive
            shutil.copy(script_path, destination_path)
            print(f"File successfully copied to {destination_path}")
    else:
        print("No USB drive detected. Please ensure it's connected.")

if __name__ == "__main__":
    num_copies = 10000  # Set the number of copies you want to make
    copy_self_to_usb(num_copies)
