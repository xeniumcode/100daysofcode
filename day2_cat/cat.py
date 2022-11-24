import argparse,os

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Dump the content of file to the screen")
	parser.add_argument("files",nargs="+",type=argparse.FileType("r"))
	args = parser.parse_args()
	for file in args.files :
		for line in file:
			print(line,end="")
