import subprocess, os

# Terminate already running bar instances
subprocess.Popen("killall -q polybar", shell=True).wait()

# Wait until the processes have been shut down
subprocess.Popen("while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done", shell=True).wait()

# Get monitors from polybar
#process = subprocess.Popen(['polybar -m'], stdout=subprocess.PIPE, shell=True)
process = subprocess.Popen(["xrandr -q | grep ' connected'"], stdout=subprocess.PIPE, 
shell=True)

for monitor in process.stdout.readlines() :
    print "Monitor found -> " + monitor.split(" ")[0]

    my_env = os.environ.copy()
    #my_env["MONITOR"] = monitor.split(":")[0]
    my_env["MONITOR"] = monitor.split(" ")[0]
    subprocess.Popen("polybar top &", env=my_env, shell=True).wait()

print "Done"
