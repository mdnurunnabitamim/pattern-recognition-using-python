import matplotlib.pyplot as plt
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms

stereo1=data.stereo_motorcycle()
stereo = stereo1[0]
astronaut = data.astronaut()
chelsea = data.chelsea()
coffee = data.coffee()

matched1 = match_histograms(astronaut, stereo, multichannel=True)
matched2 = match_histograms(chelsea, astronaut, multichannel=True)
matched3 = match_histograms(coffee, stereo, multichannel=True)
matched4 = match_histograms(astronaut, matched3, multichannel=True)
matched5 = match_histograms(chelsea, matched4, multichannel=True)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),sharex=True, sharey=True)
for aa in (ax1, ax2, ax3): aa.set_axis_off()

ax1.imshow(astronaut)
ax1.set_title('Source')
ax2.imshow(stereo)
ax2.set_title('Ref1')
ax3.imshow(matched1)
ax3.set_title('matched1')

fig1, (ax4, ax5) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),sharex=True, sharey=True)
for aa in (ax4, ax5): aa.set_axis_off()

ax4.imshow(chelsea)
ax4.set_title('Ref2')
ax5.imshow(matched2)
ax5.set_title('Matched2')

fig2, (ax6, ax7) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),sharex=True, sharey=True)
for aa in (ax6, ax7,): aa.set_axis_off()

ax6.imshow(coffee)
ax6.set_title('Ref3')
ax7.imshow(matched4)
ax7.set_title('Matched3')

fig3, (ax8, ax9) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),sharex=True, sharey=True)
for aa in (ax8, ax9): aa.set_axis_off()

ax8.imshow(matched3)
ax8.set_title('ref4')
ax9.imshow(matched4)
ax9.set_title('Matched4')

fig4, (ax10, ax11) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3),sharex=True, sharey=True)
for aa in (ax10, ax11): aa.set_axis_off()

ax10.imshow(matched4)
ax10.set_title('Source5')
ax11.imshow(matched5)
ax11.set_title('Matched5')

plt.tight_layout()
plt.show()