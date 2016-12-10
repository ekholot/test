echo "Starting..."
for file in human_chr*.txt
do
cat header.txt $file > "$1"/$file
done
