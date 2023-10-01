### SlideServe

A simple tool that converts PowerPoint presentations into images and serves them via a FastAPI web server.

### Description

This project allows users to easily convert PowerPoint (PPT) presentations into a collection of images, and then serves these images through a responsive API built with FastAPI. Just upload your PPT files, and access the converted slides as images via API endpoints!

### Installation

Clone this repository:

```bash
git clone https://github.com/msalvaris/SlideServe.git
cd yourprojectname
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage

1. **Convert PPT to Images:**

   Run the conversion script to turn your PowerPoint files into images:

   ```bash
   python convert_ppt_to_images.py --input path/to/ppt/files --output path/to/save/images
   ```

   Replace "path/to/ppt/files" with the path containing your PPT files and "path/to/save/images" with the path where you want to save the converted images.

2. **Start FastAPI Server:**

   Run the FastAPI application:

   ```bash
   uvicorn app:app --reload
   ```

   This will start the server on http://127.0.0.1:8000/. You can access the API documentation at http://127.0.0.1:8000/docs.

3. **Access the Images via API:**

   Use the `/slides/{filename}` endpoint to access individual images, replacing `{filename}` with the actual file name of the image you want to access.

### Endpoints

- **GET** `/slides/{filename}`: Retrieve an image by its filename.
- **GET** `/slides/all`: Retrieve the list of all available images.

### Built With

- [Python](https://www.python.org/) - The programming language used.
- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used for the API.
- [python-pptx](https://python-pptx.readthedocs.io/) - Used to read PowerPoint files.
- [comtypes](https://pythonhosted.org/comtypes/) - Used to read PowerPoint on windows.
- [Pillow](https://pillow.readthedocs.io/) - Used for image processing.

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


