# Convert TabExtend exported JSON to bookmark.html

### Project Status: MVP / Proof of Concept

### Purpose
Convert TabExtend data to html for viewing in a browser as well as for importing directly into browser bookmarks.  The resulting bookmarks.html and the Chrome bookmarks can be viewed in a mobile browser, extending the basic bookmarking functionality of TabExtend to mobile.

### Need:
Users are able to export their data from TabExtend but it's difficult to get the bookmarks back into Chrome or other web browsers.  It's also not currently convenient to view the data while on a mobile device.

### Concept: 
Create a quick script to do the conversion. The resulting bookmark.html can be viewed in any browser and is formatted to be compatible with Chrome's Bookmark Manager's import command.

### Current Limitations:
1. TabExtend exported JSON doesn't currently contain the name of the categories. It just holds a semi-numeric `categoryID`. Thus, the root directory will have semi-random category names (they can be renamed later). All the table and stack names are maintained.
2. import file needs to be named `tabExtend_data.json` and in the project's base directory.
3. export file will be named `bookmark.html`
4. script only parses for bookmarks. Notes and other metadata are ignored and untested.  They may even cause the script to fail to run.

### Future Direction:
1. Add requirements.txt /environment.yml
2. refactor the processing code into an importable class
3. refactor to separate reading of the data from formating the output, using a class to store interim data
4. add basic command line argument parsing
5. possibles:
   1. web application
   2. local executables
   3. dockerization

### How to use:
1. Make sure you have a python environment with Pandas
2. Place your `tabExtend_data.json` file in the current directory
3. run or the python script `python TabExtend2HTML.py`
4. If sucessful, the `bookmarks.html` will be placed in your current directory
5. optional: open the bookmarks.html file in your browser
6. optional: Use the Bookmark Manager of your browser (Chrome tested) to import your bookmarks while maintaining a tree directory structure similar to the TabExtend organization.