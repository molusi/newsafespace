import tinify as tinify
from glob import glob
import os.path

tinify.key = "TxkRT8fyVQJ0cLcn1X4KB3r7d6M8bM9T"
with open("media/blog_images/download.png", "rb") as source:
    source_data = source.read()
    result_data = tinify.from_buffer(source_data).to_buffer()

    source = tinify.from_url("https://tinypng.com/images/panda-happy.png")
    source.to_file("optimized.png")



source_dir_name = 'src'
destination_dir_name = 'dist'
# get all files names in directory
files = glob(source_dir_name + "/*")
# compress all files
for file in files:
    print("compressing " + file)
    source = tinify.from_file(file)
    file_name, ext = os.path.splitext(file)
    file_name = file_name.replace(source_dir_name + "/", "")
    source.to_file(destination_dir_name + "/" + file_name + ".png")
print("compressed all images")