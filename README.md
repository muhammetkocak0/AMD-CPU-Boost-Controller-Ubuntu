# AMD Turbo Boost Controller
![Screencast-from-2024-06-23-21-04-15](https://github.com/muhammetkocak0/AMD-CPU-Boost-Controller-Ubuntu/assets/76121221/9c4c5631-a182-479c-99fc-e0d822244200)
## Introduction
AMD Turbo Boost Controller is a system tray application designed specifically for Ubuntu systems. It allows users to monitor and control the AMD CPU turbo boost feature directly from the system tray.

## Prerequisites
- Ubuntu Linux with GTK+ 3.0 and AppIndicator3 support.
- Administrative privileges on the machine.

## Installation
To install the AMD Turbo Boost Indicator on Ubuntu, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/amd-turbo-boost-indicator.git
   ```
2. Change into the repository directory:
    ```bash
    cd amd-turbo-boost-indicator
    ```
3. Install necessary libraries (if not already installed):
    ```bash
    sudo apt-get install gir1.2-appindicator3-0.1 gir1.2-gtk-3.0
    ```
4. Run the application:
    ```bash
    python3 indicator.py
    ```
## Configuring Startup
**Using Startup Applications (Recommended for Ubuntu Desktop)**: Ubuntu provides a user-friendly way to manage startup applications through a GUI:
- Press Super (Windows key) and search for "Startup Applications".
- Click "Add" and enter the following details:
- Name: AMD Turbo Boost Indicator
- Command: python3 /path/to/indicator.py
- Comment: Controls AMD CPU Turbo Boost feature
- Replace /path/to/indicator.py with the actual path to the script. Click "Add" and then "Close" to save your settings.

**Systemd Method (Advanced Users)**: For users comfortable with systemd, you can set up a service to manage the application:
1. Create a systemd service file:
    ```bash
    sudo nano /etc/systemd/system/amd-indicator.service
    ```
2. Add the following configuration:
    ```bash
    [Unit]
    Description=AMD Turbo Boost Indicator
    After=graphical.target

    [Service]
    Type=simple
    ExecStart=/usr/bin/python3 /path/to/indicator.py

    [Install]
    WantedBy=default.target
    ```
3. Enable the service to start at boot:
    ```bash
    sudo systemctl enable amd-indicator.service
    ```


