import psutil 
import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/')
    cpu_cores = psutil.cpu_count(logical=True)
    net_io = psutil.net_io_counters()
    uptime = time.time() - psutil.boot_time()
    process_count = len(psutil.pids())
    swap = psutil.swap_memory()

    message = None
    if cpu_percent > 80:
        message = "High CPU Usage"
    elif mem_percent > 80:
        message = "High Memory Usage"

    return render_template("index.html",
        cpu_percent=cpu_percent,
        mem_percent=mem_percent,
        disk_percent=disk_usage.percent,
        cpu_cores=cpu_cores,
        bytes_sent=net_io.bytes_sent,
        bytes_recv=net_io.bytes_recv,
        uptime=uptime,
        process_count=process_count,
        swap_percent=swap.percent,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
