import requests
from PIL import Image


selectlist = ['Hedgehog', 'Dog', 'Cat', 'Goat', 'Cow', 'Fish', 'Highlandcow', 'Pig', 'Duck', 'Piglet','Exit']

def image_selector():
    print(f'Select from the list: \n {selectlist}. \nor enter your own input.')

    ans = input().capitalize()

    if 'Close' in ans or 'Exit' in ans:
        exit()
    else:
        print(f"Please wait whilst we load a image of {ans.title()}")
        image_generator(ans)

def image_generator(txt):
    response = requests.get(
        "https://source.unsplash.com/1920x1080?{0}".format(txt)
    )
    file = open('image.jpg', 'wb')
    file.write(response.content)
    img = Image.open(r"image.jpg")
    img.show()
    file.close()
    image_selector()


image_selector()
