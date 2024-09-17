## ssh_manager

<p align="center">
    <img style="border-radius: 20px; max-width: 100%" src=".github/static/preview.png">
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


## Deploying

Normally it works only on UNIX-like systems due to envvars,
sshpass and simple-term-menu OS support, but everything is possible...

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

#### Install shell script

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

## Configuration

As mentioned before ssh_manager aims to rename TMUX active window and close pane at session disconnect.
There's a few options how to configure that behavior:

### Launch arguments

`@ ssh_m -R` - *[**R**]ename - will prevent ssh_manager renaming active TMUX window*

- Is alternative to `$SSH_M_R` environment variable. Could be any value except empty

`@ ssh_m -C` - *[**C**]lose - will prevent ssh_manager closing pane after SSH terminated*

- Is alternative to `$SSH_M_C` environment variable. Could be any value except empty

## Important notes

- Keep in mind that environment variable `$servernickname_user` is **REQUIRED**

- ssh_manager by default is checking whether running inside TMUX, and applies those actions to it
	- Renaming current window to active ssh session
	- Termination shell on ssh disconnect
