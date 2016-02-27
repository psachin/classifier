from setuptools import setup

<<<<<<< HEAD
setup(name="classifier",
      version="1.5.1",
      description="Classify the files in your Downloads folder into suitable destinations.",
      url="http://github.com/bhrigu123/classifier",
      author="Bhrigu Srivastava",
      author_email="captain.bhrigu@gmail.com",
      license='MIT',
      package_dir={'classifier': 'src'},
      packages=['classifier'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'classifier=classifier:main',
          ],
      },
=======
setup(
        name="classifier",
        version="1.6.3",
        description="Classify the files in your Downloads folder into suitable destinations.",
        url="http://github.com/bhrigu123/classifier",
        author="Bhrigu Srivastava",
        author_email="captain.bhrigu@gmail.com",
        license='MIT',
        packages=["classifier"],
        entry_points="""
             [console_scripts]
             classifier = classifier.classifier:main
        """,
        install_requires=[
            'arrow',
            'six>=1.10.0',
        ],
        zip_safe=False
>>>>>>> 20aabcaf5df9da3f0d9b0be178ff990561e40dae
)
