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

Normally it works only on UNIX-like systems due to envvars, sshpass and simple-term-menu OS support, but everything is possible...

## 1. Environment

- sshpass - Non-interactive ssh password authentication

- Python 3 > 3.10
 
- $servernickname_user - Environment variable stores the password
	- Can be installed to .zshrc / .bashrc from special branch

### Install dependencies

`sudo apt install sshpass`

- `sshpass -V` *(Verify sshpass installation)*

`sudo apt install python3.10`

- `python3.10 -V` *(Verify python installation)*

`git clone -b shellscript https://github.com/LoliPain/ssh_manager`

`cd ssh_manager`

`python3 main.py`

- Follow the steps in script

	- Reload shell
	(`source ~/.bashrc` **/** `source ~/.zshrc`)

 -----

Now you can export passwords from specified folder using in your shell:
```
servernickname username

> Exported username@servernickname password

```

## 2. Installation

- Clone the repo
	
```
git clone https://github.com/LoliPain/ssh_manager
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

- Keep in mind that environment variable `$servernickname_user` is **REQUIRED**

- ssh_manager is checking whether running inside TMUX, and applies those actions to it
	- Renaming current window to active ssh session
	- Termination shell on ssh disconnect
