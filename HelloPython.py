import os

print os.getpid()

pid = os.fork()

if pid == 0:
    print 'child : pid = %d, ppid = %d' % (os.getpid(), os.getppid())
else:
    'pid = %d, ppid = %d' % (os.getpid(), os.getppid())