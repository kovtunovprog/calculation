from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
from signal import SIGTERM


def kill_server_process():
    for proc in process_iter():
        if proc.name() == 'Python':
            for conn in proc.connections():
                if conn.laddr.port == 8000:
                    proc.send_signal(SIGTERM)