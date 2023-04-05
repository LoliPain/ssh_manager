import os

server_nickname = input("Enter alias for remote: ")

print(
    "\n\nEnter absolute path to stored password\n"
    "e.g. for user `root`, password should be stored in file named `root` in SPECIFIED directory\n\n"
    "Path: ",
    end=None
)
keys_folder = input()

if keys_folder.endswith('/'):
    keys_folder = keys_folder[:-1]

with open("func.template", 'r') as t:
    updated_template = t.read()

updated_template = updated_template.replace('func:template', server_nickname)
updated_template = updated_template.replace('servername:template', server_nickname)
updated_template = updated_template.replace('folder:template', keys_folder)

shell_in_use = os.environ.get('SHELL')

match shell_in_use:
    case '/bin/zsh':
        with open(os.path.expanduser("~/.zshrc"), 'a') as c:
            c.write(updated_template)
    case '/bin/bash':
        with open(os.path.expanduser("~/.bashrc"), 'a') as c:
            c.write(updated_template)
    case _:
        print(f"{shell_in_use} shell isn't supported :(")
