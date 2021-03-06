import os
import xml.etree.ElementTree as ET

datafile1 = os.popen('find . -name AndroidManifest.xml').read().strip()
datafile2 = os.popen('find ../a -name AndroidManifest.xml').read().strip()

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
