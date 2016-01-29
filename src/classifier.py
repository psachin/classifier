#!/usr/bin/env python

import os


def move_to(filename, src, dest):
        if not os.path.exists(dest):
                os.makedirs(dest)

        src = os.path.join(src, filename)
        dest = os.path.join(dest, filename)

        os.rename(src, dest)

def classify(formats, output):
	print("Classfiying files..")

	cwd = os.getcwd()

	for file in os.listdir(cwd):
		filename, file_ext = os.path.splitext(file)
		file_ext = file_ext.lower()

		for folder, ext_list in list(formats.items()):
			folder = os.path.join(output, folder)

			if file_ext in ext_list:
				move_to(file, cwd, folder)

	print("Done!")
