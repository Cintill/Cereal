#  Cereal Compiler & Executor v0.1-beta
#  Copyright (C) 2022 Cintill Inc.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  GNU General Public License for more details.
#  https://www.gnu.org/licenses/gpl.html

import sys

def run(filename, devmode):
  commandsComingSoon = ["add", "sub", "mul", "div", "cv", "if", "eif", "pkg", "loop", "eloop"]
  vars = {}
  def varout(var):
    try:
      return vars[var]
    except:
      print("Error: Variable doesn't exist: %s" % var)
      sys.exit(1)
  def varin(name, value):
    vars[name] = value
  with open(filename) as f:
    #split to lines
    lines = f.read().split("\n")
    #format lines
    for line in range(len(lines)):
      lines[line] = lines[line].split(" ")
    #run code
    for line in lines:
      #put code here
      if line[0] == "out":
        if ";;" in line[1]:
          print(varout(line[1].split(";;")[1]))
        else:
          tto = ""
          for i in range(len(line)-1):
            tto += line[i+1]+" "
          print(tto)
      elif line[0] == "vs":
        args = line[1].split(";;")
        text = ""
        for i in range(len(args)-1):
          text += args[i+1]+" "
        for i in range(len(line)-2):
          text += line[i+2]+" "
        text = text[:-1]
        #print(text)
        varin(args[0], text)
      elif line[0] == "vi":
        args = line[1].split(";;")
        varin(args[0], int(args[1]))
      elif line[0] == "in":
        args = line[1].split(";;")
        text = ""
        for i in range(len(args)-1):
          text += args[i+1]+" "
        for i in range(len(line)-2):
          text += line[i+2]+" "
        text = text[:-1]
        inp = input(text)
        varin(args[0], inp)
      else:
        if line[0] in commandsComingSoon:
          print("Error: Command coming soon: "+line[0])
          sys.exit(1)
        print("Error: Unknown command: "+line[0])
        sys.exit(1)
    if devmode == "--devmode" or devmode == "-d":
      print(lines)
      print(vars)

if __name__ == "__main__":
  #main thing i guess
  if len(sys.argv) < 2:
    print("Usages: cereal [filename]")
    sys.exit(1)
  if ".cr" in sys.argv[1]:
    if len(sys.argv) == 3:
      run(sys.argv[1], sys.argv[2])
    else:
      run(sys.argv[1], "")
  else:
    print("Not a valid file\nPlease use files with the extension \".cr\"")