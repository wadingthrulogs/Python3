import os
import uuid
import random
count = 0



while count < 500:
    r1 = random.randrange(1048576,2097152)
    filename = str(uuid.uuid4())
    with open(filename, 'wb') as fout:
        fout.write(os.urandom(r1))  # replace 1024 with size_kb if not unreasonably large
    count = count + 1
else:
    print('files made')