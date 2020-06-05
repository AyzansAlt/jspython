def setup():
    import os

    print("installing modules...")
    cmds = [
        "pip install setuptools",
        "pip install twine",
        "pip install wheel",
        "python3 setup.py sdist bdist_wheel",
        # username and api token required for installing
        # so that users won't enter this repl and start
        # messing up my files.
    ]
    for i in cmds:
        os.system(i)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLogin:")
    os.system("python3 -m twine upload --repository testpypi dist/*")

input("[ENTER]")
setup()