import time

start = time.time()

# your code
nehal = 'oprs'
if nehal in open('Practical1.pdf','r').read():
    print('word exists')
else:
    print('word doesnot exists') 
# end

print(f'Time: {time.time() - start}')