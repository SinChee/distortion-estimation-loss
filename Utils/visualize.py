import matplotlib.pyplot as plt


def visualize(cleanX, cleanY, noisyX, noisyY, title = "Plot of Pixel Probability against Image Gradient"):
    pixel = range(-255, 256)
    
    _, ax = plt.subplots(1,2, figsize=(12, 8))
    ax[0].plot(pixel, cleanX, '-b', label='Clean')
    ax[0].plot(pixel, noisyX, '-r', label='Noisy')
    ax[0].grid(True)
    ax[0].set_title(title+" at X")
    ax[0].set_xlabel("Image Gradient")
    ax[0].set_xlabel("Pixel Probability")
    ax[0].legend()
    
    ax[1].plot(pixel, cleanY, '-b', label='Clean')
    ax[1].plot(pixel, noisyY, '-r', label='Noisy')
    ax[1].grid(True)
    ax[1].set_title(title+" at Y")
    ax[1].set_xlabel("Image Gradient")
    ax[1].set_xlabel("Pixel Probability")
    ax[1].legend()
    plt.show()
