'''tips and tricks for understanding the pip installer:
https://realpython.com/what-is-pip/
In the terminal, I typed: 
echo $path

It gave me the output below. I wanted to use Python to display each on a new line.
'''
paths = '/Library/Frameworks/Python.framework/Versions/3.12/bin /usr/local/bin /System/Cryptexes/App/usr/bin /usr/bin /bin /usr/sbin /sbin /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin /var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin'
paths_list = paths.split(' ')
for string in paths_list:
    print(string)