git config --global user.name 'Koala'
git config --global user.email 'kendrick.yuen41@myhunter.cuny.edu'

git pull --unshallow

git remote add upstream https://github.com/wusimon51/PyHW.git
git fetch upstream

git merge --no-edit upstream/main
git push origin main