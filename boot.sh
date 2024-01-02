
#set -eu
export PATH=~/anaconda3/bin/:~/anaconda3/condabin/:${PATH}
conda init bash
conda activate py3.9

python /App/manage.py makemigrations
python /App/manage.py migrate
python /App/manage.py runserver 0.0.0.0:8080

