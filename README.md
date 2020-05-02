# image_toolkit
- Solely purposed for reshaping/grayscaling/mirroring images for an image processing pipeline project

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
