# -*- coding: utf-8 -*-
# @Author: ander
# @Date:   2021-03-23 18:33:34
# @Last Modified by:   ander
# @Last Modified time: 2021-03-26 15:46:21
import os
import zipfile


def rename_path(path):
	for file in os.scandir(path):
		if file.is_file():
			old_name = os.path.join(path, file.name)
			new_name = os.path.join(path, file.name.encode('cp437').decode('gbk'))
			os.rename(old_name, new_name)
		else:
			old_name = os.path.join(path, file.name)
			new_name = os.path.join(path, file.name.encode('cp437').decode('gbk'))
			os.rename(old_name, new_name)
			rename_path(new_name)


def unzip(file, pwd=None):
	basename, ext = os.path.splitext(file)
	if ext != '.zip':
		raise OSError(f'{file} is not a zip file.')

	if not os.path.exists(basename):
		os.mkdir(basename)

	with zipfile.ZipFile(file, 'r') as zipobj:
		zipobj.extractall(basename, pwd=pwd)

	rename_path(basename)
