Contributor Git Workflow
--
This project is used for learning purpose, so making the code faster and reliable please have a look: 

1. git clone #TODO
2. Create a new branch: `git branch <your_name>/<ticket><title>`
3. Switch from current branch to new created branch `git checkout <your_name>/<ticket><title>`
	Note: check the branch you are with `git branch -v`
4. Do the changes
5. Add your changes to the repository:
	4.1 `git add <your_files>`
	4.2 `git commit -m 'your_changes_in_repo'`
   		Note: in case you want to make a change right now, please use `git reset --soft HEAD~1`
	4.3 'git push -u origin <your_name>/<ticket><title>'
	Note: `git log` to see your latest status about your work
6. Open a Pull Request 
7. Ask for review
8. After I will dfo the review, your commit it will be merged to `Main`.