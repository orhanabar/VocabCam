
from posixpath import split


paragraf = """MIT License 
Copyright (c) 2022 orhanabar 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """

p1 = []


# .split(" ") # split içine koyulan karekter , liste içinde bölme 
p1 = paragraf.split(" ")  

for i in p1 :
    i = i.strip(".") # koyulan karekterin liste veya dizi içinde kaldırlıması
    i = i.strip(",")
    i = i.strip("()")
    i = i.strip("\"")
    i = i.strip("\n")
    i = i.strip(":")
    
    print(i)
    # muhammed şahin deneme
