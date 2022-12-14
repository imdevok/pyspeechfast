from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.5'
DESCRIPTION = 'Transcriber audio/video to text'
LONG_DESCRIPTION = 'A package that allows to transcribe audio/video to text.'

# Setting up
setup(
    name="SpeechFast",
    version=VERSION,
    author="imdevok",
    author_email="<lenyamenshov@yandex.ru>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['vosk', 'torch'],
    keywords=['python', 'video', 'text', 'speech', 'audio', 'AI'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)