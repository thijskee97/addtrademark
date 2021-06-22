import matplotlib.pyplot as plt
from PIL import Image




input = input("your Trademark: ")

for num in range(0,3):
    img = Image.open(f"{num}.jpg")
    plt.figure(figsize=(12,8))
    #Finishes drawing a picture of it. Does not display it.
    plt.imshow(img)
    for height in range(500,4000,500):
        plt.text(height, height, input, color="orange", fontdict={"fontsize":15, "fontweight":'bold', "ha":"left", "va":"baseline"})
    #Display the image
    plt.show()