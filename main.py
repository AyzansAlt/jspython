import subprocess


def setup(domain):
    import os

    print("installing modules...")
    installs = [
        "setuptools",
        "twine",
        "wheel"#,
        # "python3 setup.py sdist bdist_wheel",
        # username and api token required for installing
        # so that users won't enter this repl and start
        # messing up my files.
    ]


    for i in installs:
        subprocess.Popen(['pip', 'install', i])
    
    
    subprocess.Popen(['python3', 'setup.py', 'sdist', 'bdist_wheel'])


    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLogin:")
    os.system("python3 -m twine upload --repository " + domain + " dist/*")

uploader = input("> (testpypi, pypi) ")
input("[ENTER]") 
setup(uploader)