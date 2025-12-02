---
date created: 2025-09-17T15:02:38+02:00
date modified: 2025-09-18T10:49:50+02:00
---
# Git

## 1) Starten met GIT
   - Open lege map
   - Via Git-extension "Initialize Repository"
   - In Terminal
	`git remote add origin <git_url>`
     indien fout SSL => `git config --global http.sslVerify false`
     `git pull origin main`
    - Via Git-extension kan je de git grafisch zien (Git Graph)

## 2) .gitignore
    In deze file zet je welke files je niet wil linken

## 3) Werkwijze
    - Als een file aangepast is kan je in de git-extension onder changes de aanpassing toekenen
    - Geef uitleg aan je aanpassing
    - Druk op Commit
    - Synchroniseer

## 4)  Welke GIT's
    - https://github.com/HOOWIM00/sib
    - https://github.com/HOOWIM00/prive

## 5) Create/clone local repos (bare)
    - open in terminal de lokale map waar repos moet komen
        > git init --bare
    - open in terminal de lokale map waar de files moeten komen
        > git clone 'url' (van bovenstaande bare) <name_new_folder>

## 6. Voeg een extra remote toe
`git remote set-url --add --push origin "D:\Sibelco\Elektrische Dienst en Automatisering - Automatisering\Toepassingen\repos\sib"`
Met een gewone `git push` worden alle remotes gepushed.

## 7. Branches
git branch => kijk in welke branch je zit
git branch xxx => maak nieuwe branch aan
git checkout xxx => ga naar branch

## 8. Merge
    - Branch yyy toevoegen aan branch xxx
    - Ga naar de branch waar je naartoe wil mergen (git checkout xxx)
    - Merge een branch naar actieve branch (git merge yyy)

## 9. Git commands
| command          | action        |
| ---------------- | ------------- |
| git remote -v    | show remotes  |
| git branch       | show branch   |
| git branch xxx   | create branch |
| git checkout xxx | goto branch   |
| git merge xxx    | merge branch  |
|                  |               |