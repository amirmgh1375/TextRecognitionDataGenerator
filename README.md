# TextRecognitionDataGenerator
A synthetic data generator for text recognition with arabic and persian strings support 

## What is it for?
Generating text image samples to train an OCR software. Now supporting arabic and persian texts! For a more thorough tutorial see [the official documentation](https://textrecognitiondatagenerator.readthedocs.io/en/latest/index.html).

## What do I need to make it work?

I use Archlinux so I cannot tell if it works on Windows yet.

```
Python 3.X
OpenCV 4 (Works with 3.2, probably works with 2.4)
Pillow
Numpy
Requests
BeautifulSoup
tqdm
```

 You can simply use `pip install -r requirements.txt` too.

## New
- Add `--font` to use only one font for all the generated images
- Add `--fit` and `--margins` for finer layout control
- Change the text orientation using the `-or` parameter
- Change the space width using the `-sw` parameter
- Specify text color range using `-tc '#000000,#FFFFFF'`, please note that the quotes are **necessary**
- Explicit alignement when using `-al` with fixed width (0: Left, 1: Center, 2: Right)
- Add support for Simplified and Traditional Chinese

## How does it work?
`python run.py -w 5 -f 64`

You get 1000 randomly generated images with random text on them like:

![1](samples/1.jpg "1")
![2](samples/2.jpg "2")
![3](samples/3.jpg "3")
![4](samples/4.jpg "4")
![5](samples/5.jpg "5")

What if you want random skewing? Add `-k` and `-rk` (`python run.py -w 5 -f 64 -k 5 -rk`)

![6](samples/6.jpg "6")
![7](samples/7.jpg "7")
![8](samples/8.jpg "8")
![9](samples/9.jpg "9")
![10](samples/10.jpg "10")

But scanned document usually aren't that clear are they? Add `-bl` and `-rbl` to get gaussian blur on the generated image with user-defined radius (here 0, 1, 2, 4):

![11](samples/11.jpg "0")
![12](samples/12.jpg "1")
![13](samples/13.jpg "2")
![14](samples/14.jpg "4")

Maybe you want another background? Add `-b` to define one of the three available backgrounds: gaussian noise (0), plain white (1), quasicrystal (2) or picture (3).

![15](samples/15.jpg "0")
![16](samples/16.jpg "1")
![17](samples/17.jpg "2")
![23](samples/23.jpg "3")

When using picture background (3). A picture from the pictures/ folder will be randomly selected and the text will be written on it.

Or maybe you are working on an OCR for handwritten text? Add `-hw`! (Experimental)

![18](samples/18.jpg "0")
![19](samples/19.jpg "1")
![20](samples/20.jpg "2")
![21](samples/21.jpg "3")
![22](samples/22.jpg "4")

It uses a Tensorflow model trained using [this excellent project](https://github.com/Grzego/handwriting-generation) by Grzego.

**The project does not require TensorFlow to run if you aren't using this feature**

You can also add distorsion to the generated text with `-d` and `-do`

![23](samples/24.jpg "0")
![24](samples/25.jpg "1")
![25](samples/26.jpg "2")

The text is chosen at random in a dictionary file (that can be found in the *dicts* folder) and drawn on a white background made with Gaussian noise. The resulting image is saved as [text]\_[index].jpg

There are a lot of parameters that you can tune to get the results you want, therefore I recommand checking out `python run.py -h` for more informations.

## How to create images with Persian or Arabic (both simplified and traditional) text

It is simple! Just do `python run.py -l fa -c 1000 -w 5`!

you may have to edit `texts/cn.txt` to include some meaningful words instead of random glyphs.

Here are examples of what I could make with it:

![26](samples/32.jpg "0")
![27](samples/33.jpg "1")
![28](samples/35.jpg "2")
![29](samples/37.jpg "3")
![30](samples/38.jpg "4")
![31](samples/39.jpg "5")
![32](samples/40.jpg "6")
![33](samples/41.jpg "7")
![34](samples/42.jpg "8")
![35](samples/43.jpg "9")
![36](samples/44.jpg "10")
![37](samples/45.jpg "11")


## Can I add my own font?

Yes, the script picks a font at random from the *fonts* directory.

|||
|:----|:-----|
| fonts/latin | English, French, Spanish, German |
| fonts/fa | Persian - Arabic |
|||

Simply add / remove fonts until you get the desired output.

If you want to add a new non-latin language, the amount of work is minimal.

1. Create a new folder with your language two-letters code
2. Add a .ttf font in it
3. Edit `run.py` to add an if statement in `load_fonts()`
4. Add a text file in `dicts` with the same two-letters code
5. Run the tool as you normally would but add `-l` with your two-letters code

It only supports .ttf for now.
