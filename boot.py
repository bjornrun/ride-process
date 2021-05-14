import os
import sys
from pathvalidate import sanitize_filepath
import shutil


if __name__ == "__main__":
    if len(sys.argv) == 1:
        if os.path.exists("local"):
            shutil.rmtree("local")
        destination = shutil.copytree("localsrc/test", "local")
        print("destination: ", destination)
        os.chdir(destination)
        os.system("python main.py")
    elif len(sys.argv) == 5:
        if os.path.exists("local"):
            shutil.rmtree("local")
        code = sanitize_filepath(sys.argv[1])
        src = sanitize_filepath(sys.argv[2])
        dst = sanitize_filepath(sys.argv[3])
        model = sanitize_filepath(sys.argv[4])
        if os.path.isdir("code/{code}".format(code=code)):
            destination = shutil.copytree("code/{code}".format(code=code), "local")
            print("destination: ", destination)
            os.chdir(destination)
            os.system(
                "python main.py {src} {dst} {model}".format(
                    src=src, dst=dst, model=model
                )
            )
        else:
            print("check parameters:", code, src, dst, model)
    else:
        print("nope")
