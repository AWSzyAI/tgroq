#!/bin/sh
current_dir=$(pwd)
target_dir=${1%/}
echo "#!/bin/sh
cd \"$current_dir\"
python3 tgroq.py \"\$@\"" > tgroq.sh
chmod +x tgroq.sh
mv tgroq.sh $target_dir/tgroq