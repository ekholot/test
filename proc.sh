echo "Building plots for genom data"
echo "Starting..."
for file in "$@"
do
echo processing "$file"
python test1.py "$file"
done
echo "Done!"
