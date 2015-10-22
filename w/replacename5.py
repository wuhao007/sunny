read_file1 = open('AndroidManifest1.xml', 'r')

string1 = read_file1.read()
print string1
string2 = "Yao Chen"

def replace(string1, string2):
    app_index = string1.find('<application')
    if app_index != -1:
        name_index = string1.find('android:name', app_index)
        if name_index != -1:
            start = string1.find('"', name_index)
            end = string1.find('"', start + 1)
            return string1[:start + 1] + string2 + string1[end:]
    return string1
print replace(string1, string2)
