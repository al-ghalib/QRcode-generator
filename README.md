# QR Code Generator

## Overview

This is a simple QR code generator built using Python. It allows users to generate QR codes from text or URLs and save them as image files. The project is lightweight and easy to use, making it ideal for personal and small-scale professional use.

## Features

- Generate QR codes from any text or URL
- Save QR codes as PNG images
- Simple and user-friendly script
- No external dependencies except `qrcode` and `pillow`

## Installation

To use this QR code generator, you need to have Python installed on your system. Then, follow these steps:

1. Clone this repository:

   ```sh
   git clone https://github.com/al-ghalib/QRcode-generator.git
   cd QRcode-generator
   ```

2. Install the required dependencies:

   ```sh
   pip freeze > requirements.txt
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```sh
   python main.py
   ```
2. Enter the text or URL you want to convert into a QR code.
3. The script will generate a QR code and save it as an image file.

## Dependencies

This project requires the following Python packages:

- `qrcode`
- `pillow`

You can install them manually using:

```sh
pip install qrcode pillow
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

[al-ghalib](https://github.com/al-ghalib)

## Acknowledgments

- Inspired by various QR code generation tools
- Built with Python to provide a simple, efficient solution

