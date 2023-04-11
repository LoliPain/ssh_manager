---
name: Report an invalid or unexpected behavior
about: Something is wrong in default usage workflow that is related to current project
title: ''
labels: invalid
assignees: ''

---

## Definitely a `ssh_manager` issue

*There's a non-zero chance of your issue to pend isn't really related to `ssh_manager`, so please make sure that:*

0. *Re-read the [README](https://github.com/LoliPain/ssh_manager/blob/master/README.md) installation and configuration guide and follow all of those steps*
1. *Verify that `$servername_user` environment that should contain the password for the remote machine exists in your current shell session:*
`@ echo $servername_user`
*(Where `servername` and `user` are matching the entry in ssh_manager storage)*
2. *Verify `sshpass -p` direct connection to remote:*
`@ sshpass -p $servername_user ssh user@remoteip`
**NOTE** *that `user` in `$servername_user` should be exactly the same as `user` in `ssh user@remoteip`*
3. *Verify python installation itself:*
`@ python3 -V`
**OR**
`@ python3.x -V` *where's x is your python release*

**Checklist**:
- [ ] *My issue is not related to connection problems* **or** *I'm aware that my `ssh_manager` storage and shell environment is fine*
	- [ ] *Direct connection using `sshpass -p` is performed, but connection through `ssh_manager` seems inappropriate*
- [ ] *Broken functionality is declared and documented in the README project description*


## A detailed explanation of the issue goes here
#### Screenshots, screencasts, and other useful information are welcome
------
...
