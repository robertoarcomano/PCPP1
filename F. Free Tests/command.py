import subprocess

def decode_and_format(string):
    return string.decode("utf-8").replace("\n","")


output = subprocess.run(["find", "/etc/ssh/", "/root"], capture_output=True)
print(type(output.stdout))
print(output.stdout.decode("utf-8"))
print(output.stderr.decode("utf-8"))

output = subprocess.Popen(["find", "/etc/ssh"], stdout=subprocess.PIPE)
print(type(output.stdout))
print(output.stdout.read().decode("utf-8"))
print(output.stderr)
print()

output = subprocess.Popen(["find", "/etc/ssh"], stdout=subprocess.PIPE)
output1 = subprocess.Popen(["grep", "config"], stdout=subprocess.PIPE, stdin = output.stdout)
for line in output1.stdout.readlines():
    my_dir = decode_and_format(line)
    dir_with_size = decode_and_format(subprocess.check_output(["du", "-s", "-h", my_dir]))
    print(dir_with_size)
