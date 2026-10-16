import platform
import shutil
import psutil
import time
from datetime import datetime

while True:
    print("\033[2J\033[H", end="")
    print("=" * 40)
    print("   AWS CLOUD SERVER HEALTH MONITOR")
    print("=" * 40)

    print("Server:", platform.node())
    print("OS:", platform.system())
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("\n--- CPU ---")
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    print("CPU Cores:", psutil.cpu_count())

    print("\n--- MEMORY ---")
    memory = psutil.virtual_memory()
    print("Total RAM:", round(memory.total / (1024**3), 2), "GB")
    print("Used RAM:", round(memory.used / (1024**3), 2), "GB")
    print("RAM Usage:", memory.percent, "%")

    print("\n--- DISK ---")
    disk = shutil.disk_usage("/")
    print("Total Disk:", round(disk.total / (1024**3), 2), "GB")
    print("Used Disk:", round(disk.used / (1024**3), 2), "GB")
    print("Free Disk:", round(disk.free / (1024**3), 2), "GB")

    print("\nRefreshing every 3 seconds...")
    time.sleep(3)
