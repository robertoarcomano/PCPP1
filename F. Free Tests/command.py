import subprocess

output = subprocess.run(["find", "/etc/ssh/", "/root"], capture_output=True)
print(type(output.stdout))
print(output.stdout.decode("utf-8"))
print(output.stderr.decode("utf-8"))

output = subprocess.Popen(["find", "/etc/ssh"], stdout=subprocess.PIPE)
print(type(output.stdout))
print(output.stdout.read().decode("utf-8"))
print(output.stderr)
