import os
import comtypes.client
import glob
import json
from rich.progress import track
import imageio
import fire


def slides2images():
    # Load PowerPoint
    ppt = comtypes.client.CreateObject("PowerPoint.Application")
    ppt.Visible = 1

    # filenames = glob.glob(os.path.join("C:\\Users\\msalvaris\\Documents", "irobot_ppts", "*.pptx"))
    # output_folder = os.path.join("C:\\Users\\msalvaris\\Documents", "ppt_images")

    filenames = glob.glob(os.path.join("C:\\Users\\msalvaris\\Documents\\OneDrive_2023-09-27\\ML Team Meeting", "**", "*.pptx"), recursive=True)
    output_folder = os.path.join("C:\\Users\\msalvaris\\Documents", "ml_group_ppt_images")
    os.makedirs(output_folder, exist_ok=True)
    slide_entries = []
    
    slide_num = 0
    # for pptFile in filenames[:2]:
    for pptFile in track(filenames, description="Processing..."):
        print(pptFile)
    # Open the PowerPoint file
    # pptFile = os.path.abspath('C:\\Users\\msalvaris\\Documents\\AI IRobot (AIIR).pptx')  # replace with your file name
        pptPresentation = ppt.Presentations.Open(pptFile)

        # Export slides to images
        for i, slide in enumerate(pptPresentation.Slides):
            slide_fname = os.path.join(output_folder, f"slide_{slide_num}.jpg")
            slide_entries.append({
                "filename": slide_fname,
                "origin_ppt": pptFile,
                "deck_slide_num": i,
                "slide_num": slide_num
            })
            slide.Export(slide_fname, 'JPG', 1920, 1080)  # you can adjust the resolution
            slide_num+=1
        # Close the PowerPoint file
        pptPresentation.Close()

    # Quit PowerPoint
    ppt.Quit()
    # Writing list to json
    with open(os.path.join(output_folder,"index.json"), 'w') as json_file:
        json.dump(slide_entries, json_file, indent=4)

def create_movie(image_directory, savename, fps=5):
    filenames = sorted(glob.glob(os.path.join(image_directory, "*.jpg"), recursive=False))

    # Create a writer object
    # Specify the desired output movie file and the FPS (frames per second)
    writer = imageio.get_writer(savename, fps=fps)

    # Read each image file and write it to the movie file
    for filename in track(filenames, description="Processing..."):
        image = imageio.imread(filename)
        writer.append_data(image)

    # Close the writer to finalize the movie file
    writer.close()

    print(f"Movie created: {savename}")


if __name__=="__main__":
    fire.Fire({
        "create-movie": create_movie,
        "slide2images": slides2images
    })