PATH_TO_GOLLY="/usr/share/"

sudo cp -r ./golly/Patterns $PATH_TO_GOLLY"golly/"
sudo cp -r ./golly/Rules $PATH_TO_GOLLY"golly/"

sudo cp --parents `find ./golly/Scripts/Python -name \*.py` $PATH_TO_GOLLY
