## ssh_manager

##### - Keep all ssh connection next to you
*And don't distract on password prompts*

```
ssh_manager: 

usage: ssh_m [-h] [-n]

optional arguments:
  -h, --help  show this help message and exit
  -n 
```


## Deploying

Normally it works only on UNIX-like systems due to envvars, but who knows...

## 1. Enviroment

- sshpass - Non-interactive ssh password authentication

```
sudo apt install sshpass

sshpass -V
```
 
- $nickname_user - Enviroment variable stores the password
	- Can be installed to .zshrc / .bashrc from special branch

```
git clone -b shellscript https://1dev.lolipa.in/misc/ssh_manager

./install_func.sh

Set your host nickname

Then specify the path to user-as-file password directory

Reload shell
```

## 2. Installation

- Clone the repo
	
```
git clone https://1dev.lolipa.in/misc/ssh_manager
```

- Install it system-wide

```
cd ssh_manager

python3 -m pip install .

```

- Remove the sources

```
cd ..

rm -rf ssh_manager
```

## 3. Usage

- Remote selection:

```
@ ssh_m

 -----

ssh_manager: 

> sweety@lolipa.in
  milk@simplifymilk.local
```

- Add new remote 

```
@ ssh_m -n

 -----

ssh_manager: 

Hostname (eg. google.com): simplifymilk.local
Remote user: test
Name of remote using for stored password (and env variable): simmilk

 -----

> sweety@lolipa.in
  milk@simplifymilk.local
  test@simplifymilk.local

```

## Important notes

- Keep in mind that enviroment variable `$nick_user` is **REQUIRED**

- ssh_manager is checking whether or not running inside TMUX, and applies those actions to it
	- Renaming current window to active ssh session
	- Termination shell on ssh disconnect


