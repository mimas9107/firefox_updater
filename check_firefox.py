#!/usr/bin/env python
import os

command = "which firefox"
lines = os.popen(command).readlines()
print(lines[0].rstrip("\n"))
cur_firefox_path:str=lines[0].rstrip("\n")

command = lines[0].rstrip("\n") + " --version"
lines = os.popen(command).readlines()
print(lines[0].rstrip("\n").split(" ")[-1])
cur_firefox_ver:str=lines[0].rstrip("\n").split(" ")[-1]

command = "curl \'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US\' \
  -H \'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\' \
  -H \'Accept-Language: en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ja;q=0.6\' \
  -H \'Connection: keep-alive\' \
  -H \'DNT: 1\' \
  -H \'Referer: https://www.mozilla.org/\' \
  -H \'Sec-Fetch-Dest: document\' \
  -H \'Sec-Fetch-Mode: navigate\' \
  -H \'Sec-Fetch-Site: same-site\' \
  -H \'Sec-Fetch-User: ?1\' \
  -H \'Upgrade-Insecure-Requests: 1\' \
  -H \'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36\' \
  -H \'sec-ch-ua: \"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"' \
  -H \'sec-ch-ua-mobile: ?0\' \
  -H \'sec-ch-ua-platform: \"Linux\"\'"

lines = os.popen(command).readlines()
print(lines[0].split("\"")[1])
firefox_download_link:str=lines[0].split("\"")[1]
firefox_download_ver:str=firefox_download_link.split("/")[-1].split(".tar.bz2")[0].split("-")[-1]
print(firefox_download_ver)

if (cur_firefox_ver == firefox_download_ver):
    print("same version! done")
else:
    print("Download new version!")
    command = "wget -c " + firefox_download_link
    #os.popen(command)
    os.system(command)
    if ("tar.bz2" in firefox_download_link.split("/")[-1]):
        firefox_filename = firefox_download_link.split("/")[-1]
    if os.path.exists(firefox_filename):
        print("The file {} exists".format(firefox_filename))
        print("THe downloaded file will be extracted by administrator. >>")
        os.system("sudo tar jxvf {}".format(firefox_filename))
        #os.popen("tar jxvf {}".format(firefox_filename))
        if os.path.isdir("firefox"):
            print("Moving the firefox folder to...")
            target_dir = input("Please input the directory where you wanna put>>")
            if target_dir == "":
                target_dir = "/opt/"
                print("default directory is {}".format(target_dir))
            #os.popen("mv firefox {}".format(target_dir))
            os.system("sudo mv firefox {}".format(target_dir))
    else:
        print("The file {} doesn't exist".format(firefox_filename))
