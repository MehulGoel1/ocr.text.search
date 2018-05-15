
This allows to search text among all the image (screenshot) files in a specified folder and it returns a list of file names in which all, it found the text. It runs ocr always on just the newly added files for lesser time consumption. When any screenshots or images are removed from the folder thier corresponding text file is archived not deleted, and hence they not searched for the text.


## Demo  'to be posted later' :point_left:
![](http://i.imgur.com/'fill this')

## Features

- Written in Python3
- Works on the following - image types: jpg, png, bmp, tif
- Works on Linux and Mac.

## Installation

```bash
$ sudo apt update 
$ sudo apt-get install tesseract-ocr
$ git clone https://github.com/MehulGoel1/batch.screenshot.text.search.ocr.robust
$ cd screenshot.ocr.search.robust/
```

## Usage

### Enter the path of directory containing screenshots

```bash
$ python3 runthis.py
Enter directory path to search : /home/user/Desktop/oldscreenshots/
```

### Enter a text to search :

```bash
Enter string to search : whatsapp
```

### Get a list of screenshots with the line containing that text

```bash
Screenshot_90.png 
Screenshot_171.png 
```

### Working

- This facilitates searching text among all screenshots contained in any given folder. The folder can also have other types of files as well. 

- When any of the screenshots are deleted from this folder its corresponding ocr text file are archived.

- Every time this script runs it finds the screenshots it does not have a ocr text file for and runs ocr only on those and leaves the other text files as it is.

- Hence, the search for text is always made on the screenshots only currently present in the given folder.

- For any duplicate file name conflict in the archive folder, the (2), (3) ..so on.. is added with the file name, then its stored in Archive.

- Its expected that there will be no duplicate files in the given folder because the Operating System should/will not have allowed that in the first place.

## Contributing

Use the [issue tracker](https://github.com/mehul-goel/screenshot.ocr.search.robust) to file bugs or push new features.

## License

Open sourced under the **MIT License**

search text in a batch of screenshots ocr a batch of screenshots search text in images. Written just to increase search engine accessibility (Also this is one of the many ways I tried to search the internet to find this software)
