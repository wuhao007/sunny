read_file2 = open('AndroidManifest2.xml', 'r')
read_file1 = open('AndroidManifest1.xml', 'r')
write_file = open('AndroidManifest3.xml', 'w')

app_flag = False
name = None
for line in read_file2.readlines():
    if not app_flag and '<application' in line:
        app_flag = True
    if app_flag:
        index = line.find('android:name')
        if index != -1:
            start = line.find('"', index)
            end = line.find('"', start + 1)
            name = line[start+1:end]
    if app_flag and ">" in line:
        app_flag = False
        break
print name

app_flag = False
for line in read_file1.readlines():
    if not app_flag and '<application' in line:
        app_flag = True
    if app_flag:
        index = line.find('android:name')
        if index != -1:
            start = line.find('"', index)
            end = line.find('"', start + 1)
            write_file.write(line[:start+1] + name + line[end:])
            continue
    if app_flag and ">" in line:
        app_flag = False
    write_file.write(line)
read_file1.close()
read_file2.close()
write_file.close()
    
