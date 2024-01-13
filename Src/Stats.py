import paramiko
import json
import psutil

def fetch_server_stats(node):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(node['ssh']['host'], port=node['ssh']['port'], username=node['ssh']['username'], password=node['ssh']['password'])
        stdin, stdout, stderr = ssh.exec_command('free -m && df -h')

        output = stdout.read().decode('utf-8')
        if not output:
            raise Exception("No output received")

        lines = output.split('\n')

        # Get RAM data
        ram_data = lines[1].split()

        # Get Disk data
        disk_line = [line for line in lines[2:] if line.startswith('/')]
        if not disk_line:
            raise Exception("Disk data not found")

        disk_data = disk_line[0].split()

        # Get CPU data using psutil
        cpu_percent = psutil.cpu_percent()

        stats = {
            'Name': node['name'],
            'Total Ram': ram_data[1],
            'Total Disk': disk_data[1],
            'Total Cpu': 100.0 - cpu_percent,
            'Used Ram': ram_data[2],
            'Used Disk': disk_data[2],
            'Used Cpu': cpu_percent,
            'Free Ram': ram_data[3],
            'Free Disk': disk_data[3],
            'Free Cpu': 100.0 - cpu_percent
        }

        return stats

    except Exception as e:
        return {'Name': node['name'], 'Error': str(e)}

    finally:
        ssh.close()
