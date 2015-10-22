import os
import xml.etree.ElementTree as ET

datafilelist = os.popen('find . -name AndroidManifest.xml').read().split()
datefile1 = None
datefile2 = None
for datafile in datafilelist:
    if '/w' in datafile:
        datafile1 = datafile
    if '/a/b' in datafile:
        datafile2 = datafile

print datafile1, datafile2

xmlns = "http://schemas.android.com/apk/res/android"
ET.register_namespace("android", xmlns)
key = "{" + xmlns + "}name"

tree2 = ET.parse(datafile2)
root2 = tree2.getroot()
name = None
for child in root2.iter("application"):
    if key in child.keys():
        name = child.attrib[key]
print name

tree1 = ET.parse(datafile1)
root1 = tree1.getroot()
for child in root1.iter("application"):
    if key in child.keys():
        child.set(key, name)
tree1.write(datafile1)
