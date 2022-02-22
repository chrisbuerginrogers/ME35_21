import subprocess,shlex

global process

def init(command_line):
    global process
    args = shlex.split(command_line)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell = True,universal_newlines=True)
    return command_line

def checkProcess():
    return_code = process.poll()
    if return_code is not None:
        reply = 'RETURN CODE %d \n' % return_code
        answer =  process.stdout.readlines() + process.stderr.readlines() + [reply,]
        process.kill()
        return answer
    return []

def readProcess():
#    return process.communicate(timeout = 1)
    return process.stdout.readline() + process.stderr.readline()
