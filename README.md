AWS Cloud Server Health Monitor 🚀

A Python-based server monitoring project running on AWS EC2 Ubuntu Linux.

📌 Project Overview

This project monitors the health of an AWS EC2 server by displaying live CPU, RAM, and disk usage.

✨ Features

- Live CPU usage monitoring
- RAM usage monitoring
- Disk space monitoring
- Server hostname and operating system details
- Automatic refresh every 3 seconds

🛠️ Technologies Used

- AWS EC2
- Ubuntu Linux
- Python 3
- psutil
- MobaXterm
- GitHub

▶️ How to Run

sudo apt update
sudo apt install -y python3 python3-venv
cd ~/cloud-monitor
python3 -m venv venv
source venv/bin/activate
pip install psutil
python monitor.py

👨‍💻 Author

Bhushan Chaudhari

Aspiring AWS Cloud & DevOps Engineer
