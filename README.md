## ssh_manager
![Master Status](https://img.shields.io/github/check-runs/LoliPain/ssh_manager/master?nameFilter=run_py&style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPg0KPHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0wLjc5MjcyNSAxMi4yOTI5TDUuMDg1NjIgOC4wMDAwMkwwLjc5MjcyNSAzLjcwNzEyTDIuMjA2OTQgMi4yOTI5MUw3LjkxNDA1IDguMDAwMDJMMi4yMDY5NCAxMy43MDcxTDAuNzkyNzI1IDEyLjI5MjlaIiBmaWxsPSIjMDAwMDAwIi8%2BDQo8cGF0aCBkPSJNNy4wMDAwNiAxNUgxNS4wMDAxVjEzSDcuMDAwMDZWMTVaIiBmaWxsPSIjMDAwMDAwIi8%2BDQo8L3N2Zz4%3D&label=MASTER)
![PyPI - Version](https://img.shields.io/pypi/v/ssh_m?style=for-the-badge)

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


## 1. Environment
##### Since 0.2.0 ssh_manager works both on Windows and *NIX, thanks to [InquirerPy](https://github.com/kazhala/InquirerPy)

- sshpass - Non-interactive ssh password authentication

- python >= 3.10
 
- $servernickname_user - Environment variable that stores the password

### Install dependencies

`sudo apt install sshpass`

- `sshpass -V` *(Verify sshpass installation)*

- `python3 -V` *(Verify python installation, should be **greater than** 3.10)*

#### Define environment variable
```bash
myserver_root=$(cat ~/SuperSecretPasswordForRoot)

echo $myserver_root
# Here goes the password
```

## 2. Installation

As simple as:
```bash
pip install ssh_m
```

## 3. Usage

- Remote selection:
    - Simply run `ssh_m`
        ```
        > ssh_m
        ssh_manager v0.2.0:

        Select SSH user:
        >me@some.example.com
          milk@simplifymilk.local

        ```
- Add new remote 
    - `ssh_m -n`
    - Or press "n" key at `ssh_m` menu
    ```
    ssh_manager v0.2.0:

     Hostname: google.com
     Remote user: root
     Environment variable suffix: mygoogle

     -----

    > root@google.com
      milk@simplifymilk.local
      me@some.example.com
    ```
    Exampe configuration for new server `google.com`, with environment variable for it `$mygoogle_root`
- Addional controls
    - **[n]** key - Create new entry in list while in menu
    - **[d]** key - Delete hovered entry
    - **[q]** or **[Ctrl-C]** or **[Ctrl-D]** - Close ssh_manager

## Configuration

The default storage is `JSON` file type, that placing in home location:

`~/.ssh_manager_store`

##### Remember, the storage contains **NO** any sensitive information. It just a mapping for environment variable. 

Also, as mentioned before ssh_manager aims to rename TMUX active window and close pane at session disconnect.
There's a few options how to configure that behavior:

#### Launch arguments

`@ ssh_m -R` - *[**R**]ename - will prevent ssh_manager renaming active TMUX window*

- Is alternative to `$SSH_M_R` environment variable. Could be any value except empty

`@ ssh_m -C` - *[**C**]lose - will prevent ssh_manager closing pane after SSH terminated*

- Is alternative to `$SSH_M_C` environment variable. Could be any value except empty

#### Important notes

- Keep in mind that environment variable `$servernickname_user` is **REQUIRED**

- ssh_manager by default is checking whether running inside TMUX, and applies those actions to it
	- Renaming current window to active ssh session
	- Termination shell on ssh disconnect

