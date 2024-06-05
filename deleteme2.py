#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description="ECHO: python utility for displaying message on stdout \n SYNOPSIS: ECHO [MESSAGE] [OPTION]")
print(parser)
parser.add_argument("message", help="Add your message")
parser.add_argument("--twice", "-t", help="print message twice", action="store_true")
args = parser.parse_args()

if args.message:
	print(args.message)
	if args.twice:
		print(args.message)




