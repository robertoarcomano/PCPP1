import subprocess

def chop(string):
    return string.replace("\n","")

def decode(string):
    return string.decode("utf-8")

def decode_and_chop(string):
    return string.decode("utf-8").replace("\n","")


output = subprocess.run(["find", "/etc/ssh/", "/root"], capture_output=True)
print(type(output.stdout))
print(decode(output.stdout))
print(decode(output.stderr))
print()

output = subprocess.Popen(["find", "/etc/ssh"], stdout=subprocess.PIPE)
print(type(output.stdout))
print(output.stdout.read().decode("utf-8"))
print(output.stderr)
print()

output = subprocess.Popen(["find", "/etc/ssh"], stdout=subprocess.PIPE)
output1 = subprocess.Popen(["grep", "config"], stdout=subprocess.PIPE, stdin = output.stdout)
for line in output1.stdout.readlines():
    my_dir = decode_and_chop(line)
    dir_with_size = decode_and_chop(subprocess.check_output(["du", "-s", "-h", my_dir]))
    print(dir_with_size)
