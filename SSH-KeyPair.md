# SSH Key Pairs 
![Alt text](Images/sshkeypair.png)
## How to creat SSH key pair and use it with github 

### Step 1
- open up a git bash terminal 
- CD into .ssh folder 
### Step 2
- generate a key 
- `ssh-keygen -t rsa -b 4096` -C "Email adress"
- call the file github-key

## step 4 
- go to github find your settings then go to ssh and gpg keys
- title it github-key 
- then is ssh key add your public key `cat github-key.pub`
- then you need to run the command `eval 'ssh=agent -s'` makie sure to use the command next to the number one on your keyboard not the single quotes 
- then just run ssh-add github-key 

## step 5
- add private key to local host 
- run ` ssh -t git@github.com 
- you will see this come up if you have done it right 
- Hi AlexColmer! You've successfully authenticated, but GitHub does not provide shell access.
## step 6
- creating a new repo and using ssh to add content
- create a repo with test-ssh 
- create a new folder `mkdir test-ssh`
- create a new file in this folder `touch README.md`
- use this command to add content to the file `nano readme.md`
- save the change with `ctrl+x` `Y` then `enter 
- use `cat then the name of the file` to see if the change has been made 

## step 6
- `git init` 'creates the hidden folder `.git` and certain files that store the changes, commits, and changes in the staged area'
- `git add .` 'checking the status of all the changes made so far in the repo and making sure they are tracked by github'
- `git commit -m "notes on made changes"`, 'commits the changes made to the repo'
- `git branch -M main` 'switches the branch used to push the changes'
- `git remote add origin <the SSH path from your repo on github.com>` 'specifies the SSH version of the remote repo we want to use'
- `git push-u origin main` 'pushes the changes to the repo you picked and the branch through which you specify it'

