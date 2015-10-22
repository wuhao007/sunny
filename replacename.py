import xml.etree.ElementTree as ET

xmlns = "http://schemas.android.com/apk/res/android"
ET.register_namespace("android", xmlns)

datafile = "AndroidManifest2.xml"
tree = ET.parse(datafile)
root = tree.getroot()
key = "{" + xmlns + "}name"
name = None
for child in root.iter("application"):
    if key in child.keys():
        name = child.attrib[key]
print name

datafile = "AndroidManifest1.xml"
tree1 = ET.parse(datafile)
root1 = tree1.getroot()
for child in root1.iter("application"):
    if key in child.keys():
        child.set(key, name)
tree1.write(datafile)
