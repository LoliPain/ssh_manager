## ssh_manager
![TOML Python](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FLoliPain%2Fssh_manager%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=tool.poetry.dependencies.python&style=flat-square&logo=python&logoColor=yellow&label=Python)


![Master Status](https://img.shields.io/github/check-runs/LoliPain/ssh_manager/master?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPg0KPHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0wLjc5MjcyNSAxMi4yOTI5TDUuMDg1NjIgOC4wMDAwMkwwLjc5MjcyNSAzLjcwNzEyTDIuMjA2OTQgMi4yOTI5MUw3LjkxNDA1IDguMDAwMDJMMi4yMDY5NCAxMy43MDcxTDAuNzkyNzI1IDEyLjI5MjlaIiBmaWxsPSIjMDAwMDAwIi8%2BDQo8cGF0aCBkPSJNNy4wMDAwNiAxNUgxNS4wMDAxVjEzSDcuMDAwMDZWMTVaIiBmaWxsPSIjMDAwMDAwIi8%2BDQo8L3N2Zz4%3D&label=MASTER)
![PyPI - Version](https://img.shields.io/pypi/v/ssh_m.py?style=for-the-badge)

<p align="center">
    <img style="max-width: 100%" src=".github/static/preview.png">
</p>

##### - Keep all ssh connection next to you
*And don't distract on password prompts*

```
ssh_manager: 

usage: ssh_m [-h] [-n] [-R] [-C]

optional arguments:
  -h, --help  show this help message and exit
  -n          Proceed new SSH connection to storage Executed by default if storage is empty.
  -R          Acts same as $SSH_M_R Prevents renaming TMUX window on SSH connection.
  -C          Acts same as $SSH_M_C Prevents closing of TMUX after SSH is disconnected.
```
##### Since 0.2.0 ssh_manager works both on Windows and \*NIX, thanks to [InquirerPy](https://github.com/kazhala/InquirerPy)


## 1. Environment

##### General:
- **python3** - *is an interpreted, interactive, object-oriented, open-source programming language.*
- **ssh** - *OpenSSH-compatible client*
------
##### Password connections:
- **sshpass** - *Non-interactive ssh password authentication*
- Define user-specific environment variable
    - Unix-like:
        ```bash
        myserver_root=$(cat ~/SuperSecretPasswordForRoot)
        ```
    - Windows:
        ```bat
        $env:myserver_root=$(cat ~/SuperSecretPasswordForRoot)
        ```
------
##### SSH-key connections:
- **IdentityFile** - *Private key for remote machine, could be placed anywhere*


## 2. Install dependencies 
##### (Optional, required for password-based SSH connections)

#### Using APT:
`sudo apt install sshpass`

#### Homebrew:
`brew install sshpass`

#### Other \*NIX:
**1. [Download .tar.gz source code](https://sourceforge.net/projects/sshpass/)**

**2. Extract archive and enter directory:**
`tar -xf sshpass*.tar.gz && rm sshpass*.tar.gz && cd sshpass*`

**3. Run as following:**

```bash
./configure
make
sudo make install
```
###### Or installation without sudo-access setting the `--prefix`

#### Windows (experimental):
**1. [Download sshpass-win32](https://github.com/xhcoding/sshpass-win32)**

**2. [Optional] Check your PATH environment variable**
- **[Win + R] ->** `SystemPropertiesAdvanced.exe`
- Environment variables **-> Path ->** Edit

**3. Drop sshpass.exe to one of present folder in Path**


### Verify everything is installed properly

- `sshpass -V` *(Check, that sshpass is installed and operable)*

-   ```
    echo $myserver_root
        -----
    # Here goes the password
    ```


## 3. ssh_manager Installation

As simple as:
```bash
pip install ssh-m.py
```

## 4. Usage

- Remote selection:
    - Simply run `ssh_m`
        ```
        > ssh_m
        ssh_manager v0.x.y:

        Select SSH user:
        >me@some.example.com
          milk@simplifymilk.local

        ```
- Add new remote 
    - `ssh_m -n`
    - Or press "n" key at `ssh_m` menu
    ```
    ssh_manager v0.x.y:

     Hostname: google.com
     Remote user: root
     ? Select connection type: Env
     Environment variable prefix: mygoogle

     -----

    > root@google.com
      milk@simplifymilk.local
      me@some.example.com
    ```
    Example configuration for new server `google.com`, with environment variable for it `$mygoogle_root`
- Additional controls
    - **[n]** key - Create new entry in list while in menu
    - **[d]** key - Delete hovered entry
    - **[q]** or **[Ctrl-C]** or **[Ctrl-D]** - Close ssh_manager

## Configuration

The default storage is `JSON` file type, that placing in home location:

`~/.ssh_manager_store`

##### Remember, the storage contains **NO** any sensitive information. It just a mapping for environment variable names and paths to key files. 

Also, as mentioned before ssh_manager aims to rename TMUX active window and close pane at session disconnect.
There's a few options how to configure that behavior:

#### Launch arguments

`@ ssh_m -R` - *[**R**]ename - will prevent ssh_manager renaming active TMUX window*
- Is alternative to `$SSH_M_R` environment variable.

`@ ssh_m -C` - *[**C**]lose - will prevent ssh_manager closing pane after SSH terminated*
- Is alternative to `$SSH_M_C`.

#### Important notes

- Keep in mind that for password-based logins environment variable `$servernickname_user` is **REQUIRED**, otherwise use key-based entry

- ssh_manager by default is checking whether running inside TMUX, and applies those actions to it
	- Renaming current window to active ssh session
	- Termination shell on ssh disconnect
