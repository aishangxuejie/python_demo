import os
import shutil
import time

def mvFiles():
	source_path = os.path.abspath(r'D:\Documents\github.gif')
	target_path = os.path.abspath(r'D:\Test')
	if not os.path.exists(target_path):
		os.makedirs(target_path)
	else:
		print('The target path already exists!')
	if os.path.exists(source_path):
		path = shutil.copy(source_path, target_path)
		print('copy files finished!' + target_path)
	else:
		print('copy files fase!' + source_path)
def inputFilePath():
	print('读取需要更新的文件：')
	with open('D:\Test\lwjs_update.txt', 'r', encoding='utf-8') as line:
		for each_line in line:
			print(line.read())


if __name__ == '__main__':
	#inputFilePath()
	mvFiles()