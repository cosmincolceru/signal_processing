import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage
from scipy.fft import dctn, idctn
import cv2

Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]])


def ex1():
    X = misc.ascent()

    full_x_jpeg = np.zeros((X.shape))

    for i in range(0, len(X) // 8):
        for j in range(0, len(X[i]) // 8):
            x = X[i*8:(i + 1)*8, j*8:(j + 1)*8]
            y = dctn(x)

            y_jpeg = Q_jpeg * np.round(y / Q_jpeg)
            x_jpeg = idctn(y_jpeg)

            for k in range(8):
                for t in range(8):
                    full_x_jpeg[i*8 + k, j*8 + t] = x_jpeg[k, t]

    plt.subplot(121).imshow(X, cmap='gray')
    plt.title("Original")
    plt.subplot(122).imshow(full_x_jpeg, cmap='gray')
    plt.title("JPEG")
    plt.savefig("ex1.pdf", format="pdf")
    plt.savefig("ex1.png", format="png")
    plt.show()


def jpeg_compression_rgb(image, quantization_matrix):
    # Convert the image to YCrCb 
    ycrcb_image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
    ycrcb_image_jpeg = np.zeros((ycrcb_image.shape), dtype=np.uint8)

    for channel in range(3):
        # Compress each chaneel
        img = ycrcb_image[:, :, channel]

        for i in range(0, len(img) // 8):
            for j in range(0, len(img[i]) // 8):
                x = img[i*8:(i + 1)*8, j*8:(j + 1)*8]
                y = dctn(x)

                y_jpeg = quantization_matrix * np.round(y / quantization_matrix)
                x_jpeg = idctn(y_jpeg)

                for k in range(8):
                    for t in range(8):
                        ycrcb_image_jpeg[i*8 + k, j*8 + t, channel] = x_jpeg[k, t]

    # Convert the image back to RGB
    return cv2.cvtColor(ycrcb_image_jpeg, cv2.COLOR_YCrCb2RGB)

def ex2():
    image = misc.face(gray=False)

    image_jpeg = jpeg_compression_rgb(image, Q_jpeg)

    plt.subplot(121).imshow(image)
    plt.title("Original")
    plt.subplot(122).imshow(image_jpeg)
    plt.title("JPEG")
    plt.savefig("ex2.pdf", format="pdf")
    plt.savefig("ex2.png", format="png")    
    plt.show()


def jpeg_compression_mse_threshold(image, quantization_matrix, mse_threshold):
    Q_jpeg_copy = quantization_matrix.copy()

    while True:
        image_jpeg = jpeg_compression_rgb(image, Q_jpeg_copy)

        # Calculate MSE 
        mse = np.mean((image - image_jpeg) ** 2)

        if mse > mse_threshold:
            return image_jpeg
        else:
            Q_jpeg_copy = 2 * Q_jpeg_copy 

def ex3():
    image = misc.face(gray=False)

    image_jpeg = jpeg_compression_mse_threshold(image, Q_jpeg, 5)

    plt.subplot(121).imshow(image)
    plt.title("Original")
    plt.subplot(122).imshow(image_jpeg)
    plt.title("JPEG")
    plt.savefig("ex3.pdf", format="pdf")
    plt.savefig("ex3.png", format="png")
    plt.show()


def ex4():
    cap = cv2.VideoCapture('video.mp4')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('compressed_video.avi', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        compressed_frame = jpeg_compression_rgb(frame, Q_jpeg)
        out.write(compressed_frame)

    cap.release()
    out.release()


def main():
    ex1()
    # ex2()
    # ex3()
    # ex4()

if __name__ == "__main__":
    main()