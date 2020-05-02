# image_toolkit
- Solely purposed for reshaping/grayscaling/mirroring images for an image processing pipeline project.
    - There's a `self.image_type` that can be utilised to load `.png`,`.jpg` or other types of supported image formats by the `Pillow` library.

- Requires 3 `sys.argv`'s to run:
    - `sys.arv[1]` = input_path
        - The path in which the original images exist.
    - `sys.argv[2]` = output_path
        - The directory (needed to be created before running the script) to be saved in after retooling.
    - `sys.argv[3]` = type
        - Type of processing operation to be applied in the images

- Required packages:
    - `Pillow` : https://pypi.org/project/Pillow/2.2.1/
    
- Example run:
    - `main.bat` or `main.sh`
        - `input_path` = `.\images`
        - `ouptut_path` = `.\output`
        - `type` = `gray`
