import xml.etree.ElementTree as ET

xmlns = "http://schemas.android.com/apk/res/android"
ET.register_namespace("android", xmlns)
datafile = "AndroidManifest.xml"
tree = ET.parse(datafile)
root = tree.getroot()
key = "{" + xmlns + "}name"

for child in root.iter("application"):
    if key in child.keys():
        child.set(key, "Yao Chen Hao Wu")
tree.write(datafile + ".new")
