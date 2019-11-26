#Makes files
import os
import uuid
import random
count = 0

while count < 500:
    #file size Range in KB
    r1 = random.randrange(1048576,2097152)
    #Random file name
    filename = str(uuid.uuid4())
    with open(filename, 'wb') as fout:
        fout.write(os.urandom(r1))
    count = count + 1
else:
    print('files made')
