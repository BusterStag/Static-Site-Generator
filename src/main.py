import os
import shutil
import sys

from copystatic import *
from gencontent import *

base_dir = os.path.dirname(os.path.abspath(__file__))
dir_path_static = os.path.join(base_dir, "../static")
dir_path_public = os.path.join(base_dir, "../docs")
template_path = os.path.join(base_dir, "../template.html")
dir_path_content = os.path.join(base_dir, "../content")
default_basepath = os.path.join(base_dir, "/")

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

main()
