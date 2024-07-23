#!/usr/bin/bash
cur_firefox_location=`which firefox`
echo "Currentt firefox location: $cur_firefox_location , `file $cur_firefox_location`"
cur_firefox_ver=`firefox --version | awk -F " " '{ print $3 }'`
echo "Current firefox version : $cur_firefox_ver "


official_firefox_link=`curl 'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ja;q=0.6' \
  -H 'Connection: keep-alive' \
  -H 'DNT: 1' \
  -H 'Referer: https://www.mozilla.org/' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' | awk -F "\"" '{print $2}'`

echo "The official firefox link : $official_firefox_link "

official_firefox_ver=`python -c "print(\"$official_firefox_link\".split(\"/\")[-1].split(\".tar.bz2\")[0].split(\"-\")[-1])"`

echo $official_firefox_ver

if [ $cur_firefox_ver == $official_firefox_ver ]; then
	echo "Same with the latest version, update process was not needed"
else
	wget -c $official_firefox_link
# 	echo "aaa"
fi