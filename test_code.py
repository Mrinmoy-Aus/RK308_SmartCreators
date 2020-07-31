from matplotlib import pyplot as plt
import numpy as np

fig,axes = plt.subplots(nrows = 4, ncols = 10, figsize=(50,50))

for ax in axes.flatten():
    ax.axis('off')

##edit this line to include your own image ids
image_id_list=['{}_{}'.format(i,j) for i in range(2011,2016) for j in range(1,3)]

for i,image_id in enumerate(image_id_list):
    raw_image_path='./Images/'+ image_id +'jpg'
    raw_image = Image.open(raw_image_path)
    axes[0,i].imshow(raw_image)

    gt_image_path='./Images/'+ image_id +'jpg'
    gt_image = Image.open(gt_image_path)
    axes[0,i].imshow(gt_image)

    pre_image_path='./Images/'+ image_id +'jpg'
    pre_image = Image.open(pre_image_path)
    axes[0,i].imshow(pre_image)

    post_image_path='./Images/'+ image_id +'jpg'
    post_image = Image.open(post_image_path)
    axes[0,i].imshow(post_image)

plt.show()
