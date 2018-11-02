#!/usr/bin/python3

from lib import Interface

NAME = "TULKKI"

def main():
  interface = Interface.Interface(NAME)
  interface.run()

if __name__ == "__main__":
  main()
