#!/cygdrive/c/Users/sifat/Python38-32/python.exe


import psutil


def convert_bytes_to_gb(bytes):
    return bytes / (1048576 * 1024)


def memory_used():
    # The virtual memory is presented in bytes
    cpu_memory_bytes = psutil.virtual_memory()
    total_memory_mb = cpu_memory_bytes.total / 1048576
    available_memory_mb = cpu_memory_bytes.available / 1048576
    used_memory_mb = cpu_memory_bytes.used / 1048576

    print("Total available memory: " + str(round(total_memory_mb, 2)) + " MB")
    print("Total free memory: " + str(round(available_memory_mb, 2)) + " MB")
    print("Total used memory: " + str(round(used_memory_mb, 2)) + " MB")


def disk_quota_info():
    disk_info = psutil.disk_usage('/')
    disk_total_gb = convert_bytes_to_gb(disk_info.total)
    disk_available_gb = convert_bytes_to_gb(disk_info.free)
    disk_used_gb = convert_bytes_to_gb(disk_info.used)

    print("Total available space on computer: " + str(round(disk_total_gb, 2)) + " GB")
    print("Total free space on computer: " + str(round(disk_available_gb, 2)) + " GB")
    print("Total used space on computer: " + str(round(disk_used_gb, 2)) + " GB")


def main():
    memory_used()
    disk_quota_info()


if __name__ == "__main__":
    main()
