import platform
import psutil

print(f"CPU Usage: {psutil.cpu_percent()}%")

def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "Memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
    }

if __name__ == "__main__":
    print(get_system_info())