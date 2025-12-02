---
aliases: [git]
modified: 2025-09-13 20:25
tags: [dev, Git, workflow]
date created: 2025-02-24T00:00:00+02:00
date modified: 2025-10-01T06:53:07+02:00
---
# Git
## Flow
 - The **master** branch is used for production releases.
 - The HEAD pointer tells what is checked out
 
## Commando's
- **Current git branch**
	- `git status`
- **Create new branch**
	- `git branch my-new-branch`
- **List branches**
	- `git branch`
- **Switching branches**
	- `git checkout <other-branch>`
	- `git switch <other-branch>`

## Bare repositories
Firstly, just to check, you need to change into the directory you've created before running `git init --bare`. Also, it's conventional to give bare repositories the extension `.git`. So you can do
	  `git init --bare <new directory>`
- After creating a bare repository, add the bare directory to the active repository.

## Git ignore
  `log/*` to remove everthing 
  [Git - gitignore Documentation (git-scm.com)](https://git-scm.com/docs/gitignore)
	- created: [[2015-05-15]]T15:07:01.0000000+02:00

## git clone
  1. In a command prompt navigate to the directory where the new repository needs to be created.
  2. `git clone "\\\\tsclient\\c\\Users\\lemton00\\OneDrive - Sibelco\\DEV\\repos\\telegraf" --progress` (this can take a while even nothing is showing)

## Gui's
- ## SmartGit
  [[2016-03-21]] 14:11 =\> Begint stilaan favoriet te worden

- ## SourceTree 
  =\> Licentie in Onedrive\Apps\Sourcetree
	- [[2025-06-18]] Source gebruikt.
	
- ## GitEye 
  Heeft recente java nodig
   
  [[2015-10-10]]
  Onderzoek naar de beste git gui
- Smartgit kan je makkelijk de changes vergelijken.  
  Maar er kan maar groepen in de bovenste tree worden aangemaakt. Geen groepen in groepen
- Experiment met SourceTree. Hiermee kunnen wel subgroepen worden gemaakt

## Git submodule
  git submodule add <https://github.com/Tonny72/sibelco_configs.git> configs
	- can take a long time

## [Git - Head](dev/git/Git%20-%20Head.md)


## File protocol in GIT
- **git submodule add /submodule /project/submodule**
- fatal: transport 'file' not allowed
  fatal: clone of '/submodule' into submodule path '/project/submodule' failed
  The solution of this error is setting the global value always for file protocol in GIT like this:
- `git config --global protocol.file.allow always`

## Remove sensitive data from repo
DIT COMMANDO VERWIJDERT OOK DE FILE
```
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch path/to/your/file' --prune-empty --tag-name-filter cat -- --all
git push origin --force
```
## Add remote directory repo
- git config –global –add safe.directory

## Local config
- `git config --local user.name "Jouw Naam"`
- `git config --local user.email "jij@example.com`

## Offline install of packages
Probeer eens
```
pip download -r requirements.txt --dest /packages
```
En dan
```
pip install --no-index --no-deps
```

- ## workflow
	- Op dit (2025-07-03) moment is er geen beste manier om een gezamelijke repository te beheren.
		- 1. De ideale manier zou een fileserver zijn die toegankelijk is vanuit alle netwerken
		- 2. We kunnen repos syncen via OneDrive en hopen dat het goed blijft lopen.
		  Zie ook ((6866d576-8e79-4bd1-8727-a3e05022ce97))
		- 3. We kunnen een private git gebruiken.
### Squash bij het mergen

Als je liever niets aanpast in de feature branch zelf, kun je bij het mergen naar `main` of `develop` een squash gebruiken:

```Shell
git checkout main  
git merge --squash feature-branch  
git commit -m "Feature afgerond"  
```

Dit voegt alle wijzigingen van de feature branch samen in één commit, zonder de individuele commitgeschiedenis mee te nemen.