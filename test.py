# import os
# import json
# for filename in os.listdir('./test'):   
#     # print(os.path.join('./test', filename))
#     # # print(os.path.basename(filename))
#     # # print(os.path.splitext(filename)[0])
#     # print(os.path.splitext(filename)[0]+'.txt')
# # #    if (os.path.splitext(filename)[1]) != '.png':
# # #        print(os.path.splitext(filename)[1])
#     if (os.path.splitext(filename)[1]) != '.png':
#         with open(os.path.join('./test', filename), mode='r') as f:
#             js = f.read()
#             data = json.loads(js)
#             print((data[0]))
#             print('-------------')
#             # file1 = json.loads(file_content)
#             # print(file1)p
#     # else:
#     #     continue




# import argparse
# parser = argparse.ArgumentParser()

# parser.add_argument('-a', type=int, help='input a integer')
# args = parser.parse_args()
# print(args.a)


import os
import time
filenames = os.listdir('./test')
start = time.time()
i = 0
while(i<10):
    print(i)
    if i%2 == 0:
        i += 1
    else:
        i-=1

now = time.time()
print(now - start)
