import os
import time
import pickle
import hashlib
import argparse
import pyperclip
from pushbullet import Pushbullet

api_key = 'INSERT_API_KEY_HERE'
pickle_dump_file_path = os.path.expanduser('~/.pb_clipboard/pushbullet.pickle')

def main(title=''):
	to_push = str(pyperclip.paste())
	if len(to_push) < 1 or len(to_push) > 200:
		print('Content empty or too large to push')
		exit(0)
	try:
		with open(pickle_dump_file_path, 'rb') as pb_pickle_file:
			pb = pickle.load(pb_pickle_file)
	except:
		pb = Pushbullet(api_key)
		try:
			with open(pickle_dump_file_path, 'wb') as pb_pickle_file:
				pickle.dump(pb, pb_pickle_file)
		except:
			print('Error dumping pickle file')
	motog5 = pb.get_device('Motorola Moto G (5)')
	motog5.push_note(title, to_push)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Push clipboard content to phone')
	parser.add_argument('-t','--title', help='Title for pushbullet message', default='')

	args = parser.parse_args()
	args = vars(args)

	title = str(args.get('title')).strip()
	main(title)