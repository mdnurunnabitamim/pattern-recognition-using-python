import matplotlib.pyplot as plt
from skimage import data
from skimage import io
from skimage.color import rgb2gray
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk
from skimage.morphology import erosion, dilation, opening, closing, white_tophat

img=data.astronaut()
orig_phantom = img
grayscale = rgb2gray(orig_phantom)

horse_mask = grayscale == 0
horse_mask[45:50, 75:80] = 1

def plot_com(original,filter1,filter2,filter3,filter4,filter5,filter6,filter7,filter8,filter9,filter_name1, filter_name2, filter_name3,filter_name4,filter_name5,filter_name6,filter_name7,filter_name8,filter_name9,filter_name10):
    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10) = plt.subplots(nrows=1,ncols=10,figsize=(28, 18), sharex=True, sharey=True)

    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title(filter_name1)
    ax1.axis('off')
    ax2.imshow(filter1, cmap=plt.cm.gray)
    ax2.set_title(filter_name2)
    ax2.axis('off')
    ax3.imshow(filter2, cmap=plt.cm.gray)
    ax3.set_title(filter_name3)
    ax3.axis('off')
    ax4.imshow(filter3, cmap=plt.cm.gray)
    ax4.set_title(filter_name4)
    ax4.axis('off')
    ax5.imshow(filter4, cmap=plt.cm.gray)
    ax5.set_title(filter_name5)
    ax5.axis('off')
    ax6.imshow(filter5, cmap=plt.cm.gray)
    ax6.set_title(filter_name6)
    ax6.axis('off')
    ax7.imshow(filter6, cmap=plt.cm.gray)
    ax7.set_title(filter_name7)
    ax7.axis('off')
    ax8.imshow(filter7, cmap=plt.cm.gray)
    ax8.set_title(filter_name8)
    ax8.axis('off')
    ax9.imshow(filter8, cmap=plt.cm.gray)
    ax9.set_title(filter_name9)
    ax9.axis('off')
    ax10.imshow(filter9, cmap=plt.cm.gray)
    ax10.set_title(filter_name10)
    ax10.axis('off')

selem = disk(6)
eroded = erosion(grayscale, selem)
dilated = dilation(grayscale, selem)
opened = opening(grayscale, selem)
closed = closing(grayscale, selem)
w_tophat = white_tophat(grayscale, selem)
b_tophat = black_tophat(grayscale, selem)
sk = skeletonize(grayscale == 0)
hull1 = convex_hull_image(grayscale == 0)
hull2 = convex_hull_image(horse_mask)
plot_com(orig_phantom, eroded, dilated, opened, closed, w_tophat, b_tophat,sk,hull1,hull2,'Original', 'Eroded', 'Dilated', 'Opened', 'Closed', 'White Tophat','Black Tophat','skeletonize', 'Convex Hull1', 'Convex Hull2')

plt.show()