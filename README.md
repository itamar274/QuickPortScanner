# QuickPortScanner
Port Scanner Script
This Python script scans the first 1024 ports of a given URL to determine if each port is open or closed.

Features:
Port Scanning: Scans ports from 1 to 1024 for the specified URL.
Color-Coded Output:
Yellow: Port label
Blue: Port number
Magenta: "is" (status indicator)
Green: For open ports
Red: For closed ports
Timeout: Each connection attempt is limited to 1 second.
Requirements:
Python 3.x
colorama library (for colored terminal output)
How to Use:
Run the script in your Python environment.
When prompted, enter the URL you want to scan.
The script will check each port from 1 to 1024 and display whether it is open or closed.
Example:
kotlin
Copy code
Enter the URL you want to scan:
example.com
Port 1 is closed
Port 2 is open
Port 80 is open
