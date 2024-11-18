# list = ['def', '332', '233']
# import os 
# os.makedirs('artifacts', exist_ok=True)

# filt = os.path.join('artifacts', 'filtered_img.txt')

# with open(filt, 'w') as w:
#     for item in list:
#         w.write(f"{item}\n")

import os
f ='artifacts\datasets\train\Dog\11853.jpg '
# img_num = f.split('/')[-1].split('.')[0]
img_num = os.path.splitext(os.path.basename(f))[0]
print(img_num)