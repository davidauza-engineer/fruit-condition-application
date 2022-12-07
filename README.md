<div align="center">
  <h1><b>Fruit Condition Application</b></h1>
</div>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🙏 Resources](#resources)

# 📖 Fruit Condition Application <a name="about-project"></a>

> This project is made in the context of the `Wearable Devices and Computer Vision` course at `Harvard`.

**Fruit Condition Application** is a CLI application that detect fruits in an image, generates a Color Palette and 
determines the condition of the fruit based on the detected colors. The supported fruits in the current version are:
`apples`, `bananas`, and `oranges`.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

> Python 3.8.15 and other computer vision and machine learning libraries like `extcolors`, `imageai`, `Keras`, `opencv`,
`tensorflow`, between others. Consult `requirements.txt` for a complete list of dependencies.

### Key Features <a name="key-features"></a>

> The application determines the condition of a fruit based on the features below:

- **Object detection.**
- **Color palette generation.**
- **Determining the condition of a given banana, apple, or orange.**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💻 Getting Started <a name="getting-started"></a>

> Below you can find detailed instructions of how to run this project.

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python 3.8.15

### Setup

Clone this repository to your desired directory.

### Install

Install this project dependencies by going to the project's root directory and running:

```sh
$ pip install -r requirements.txt
```

### Usage

To run the project, execute the following command:

```sh
$ python main.py
```

When prompted to input the image path you can use the path for the images in the `test` directory. For example: 
`/Users/davidauza/Desktop/fruit-condition-application/test/banana.jpg`. The supported image formats are: `png`, `jpg`,
`jpeg`, `tiff`, `bmp`, `gif`. Also, make sure to include a valid path with no spaces in the image name.

If there is a fruit in the image the color palette for that fruit will be printed and the fruit condition will be
determined.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 👥 Authors <a name="authors"></a>

> This project was created by the Harvard students below.

👤 **David Auza**

- GitHub: [@davidauza-engineer](https://github.com/davidauza-engineer)
- Twitter: [@davidauzaeng](https://twitter.com/davidauzaeng)
- LinkedIn: [David Auza](https://www.linkedin.com/in/davidauza-engineer/)

👤 **Amna Jawad**

- GitHub: [@Amnajawad](https://github.com/Amnajawad)
- LinkedIn: [Amna Jawad](https://www.linkedin.com/in/amna-jawad-bb687078/)

👤 **Bridgette Maurer**

- GitHub: [@bmaurer2](https://github.com/bmaurer2)
- LinkedIn: [Bridgette Maurer](https://www.linkedin.com/in/bridgette-maurer/)

👤 **Jody Trumbull**

- GitHub: [@JoTeaHESFolio](https://github.com/JoTeaHESFolio)
- LinkedIn: [Jody Elizabeth Trumbull](https://www.linkedin.com/in/jodyelizabethtrumbull/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🔭 Future Features <a name="future-features"></a>

> After releasing the MVP the features below will be implemented.

- [ ] **Background removal for the cropped fruit images.**
- [ ] **Cropping the object to just generate the color palette for the very specific fruit.**
- [ ] **Support for spaces in the image path.**
 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📝 Resources <a name="resources"></a>

- [Image Color Extraction with Python in 4 Steps](https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e)
- [Object Detection with 10 lines of code](https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
