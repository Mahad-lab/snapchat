import argparse
import sys
import urllib.request

url = "https://app.snapchat.com/web/deeplink/snapcode?username={}&type={}"


def get_code(username, bitmoji=False, size=None):

	if bitmoji == False:

		# If filetype is PNG, you will get the 
		# SnapCode without the bitmoji

		filetype = "PNG"

		if size:
			url_with_size = url+"&size={}"
			request_url = url_with_size.format(username, filetype, size)
		

	else:

		# If filetype is SVG, you will get the 
		# SnapCode with the bitmoji

		filetype = "SVG"

		# Putting all the information into the url
		request_url = url.format(username, filetype)

	# Making the filename
	path = str(username) + "." + filetype.lower()

	# Downloading the image file
	urllib.request.urlretrieve(request_url, path)

	print("Downloaded ---> " + path)


def main():

	parser = argparse.ArgumentParser(description = "A simple command-line tool to download SnapChat codes.")

	parser.add_argument('username', action = "store")

	parser.add_argument("-b", "--bitmoji",
		                action= "store_true",
						help = "SnapCode with Bitmoji")

	parser.add_argument("-s", "--size",
						help = "Size of the SnapCode (pixels)")

	args = parser.parse_args()

	if len(sys.argv) == 1: # if no argument is given then show help
		parser.print_help()

	elif args.size and args.bitmoji:
		print("Sorry, you cant resize SnapCodes with Bitmoji")
		sys.exit()

	elif args.bitmoji:
		get_code(args.username, args.bitmoji)

	elif args.size:
		get_code(args.username, bitmoji=False, size=args.size)
	
	else:
		get_code(args.username)

if __name__=="__main__":
	main()
