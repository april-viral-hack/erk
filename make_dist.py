
import os
import sys
import shutil

from erk.common import *

f = open("version.txt","r")
mversion = int(f.read())
f.close()
f = open("version.txt","w")
f.write(str(mversion + 1))
f.close()


os.mkdir("./dist")
os.mkdir("./dist/settings")
os.mkdir("./dist/plugins")
os.mkdir("./dist/logs")
os.mkdir("./dist/documentation")
#os.mkdir("./dist/themes")

os.system("compile_resources.bat")

shutil.copytree("./erk", "./dist/erk",ignore=shutil.ignore_patterns('*.pyc', 'tmp*',"__pycache__"))
shutil.copytree("./themes", "./dist/themes",ignore=shutil.ignore_patterns('*.pyc', 'tmp*',"__pycache__"))

shutil.copy("./erk.py", "./dist/erk.py")
shutil.copy("./erk.ico", "./dist/erk.ico")

shutil.copy("./CHANGELOG", "./dist/CHANGELOG")
shutil.copy("./LICENSE", "./dist/LICENSE")
shutil.copy("./README.md", "./dist/README.md")
shutil.copy("./logs/logs.txt", "./dist/logs/logs.txt")
shutil.copy("./plugins/plugins.txt", "./dist/plugins/plugins.txt")
shutil.copy("./settings/settings.txt", "./dist/settings/settings.txt")

shutil.copy("./documentation/Erk-Plugin-Guide.pdf", "./dist/documentation/Erk-Plugin-Guide.pdf")

shutil.copy("./themes/themes.txt", "./dist/themes/themes.txt")


#shutil.copy("./data/user.json", "./dist/data/user.json")

os.system("powershell.exe -nologo -noprofile -command \"& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::CreateFromDirectory('dist', 'erk_dist.zip'); }\" ")

shutil.rmtree('./dist')

archive_name = f"{NORMAL_APPLICATION_NAME.lower()}-{APPLICATION_VERSION}.{str(mversion)}.zip"

os.rename('erk_dist.zip', archive_name)

shutil.copy(archive_name, "./downloads/"+archive_name)
shutil.copy(archive_name, f"./downloads/{NORMAL_APPLICATION_NAME.lower()}-latest.zip")
os.remove(archive_name)
