echo "Starting..."
for file in "$@"
do
echo processing "$file" '$file'
cat header.txt "$file" > proc/$file
done
echo "Done!"
