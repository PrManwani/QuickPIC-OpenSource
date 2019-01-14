#!/bin/sh
mkdir plots/plots54
cp rpinput plots/plots54
for item in */ ; do
		if [ "$item" != "ELOG/" ]; then
			cd $item
			for file in *.h5 ; do
				echo "$file"
				FILENAME="${file%.*}"
				#echo "$FILENAME"
				path="plots/plots54/$FILENAME.vtk"
				h5tovtk -o ../$path $file
				echo "$path"
				#echo "$item"
			done
			cd ..				
		fi
done

