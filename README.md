# mg - > The merge tool
### _command-line tool for diffing and merging text files_

__HELP__: It takes two arguments e.g "first_file.txt" and "second_file.txt"
          You will be prompted to choose __*diff*__ or __"merge"__.
          
+ "diff" just shows the differences(conflicts) between given text files
          
            + "merge" creates new merged text file and user will be prompted to resolve each conflict
          
            + if one of the text files is larger than other, user will be prompted if he wants to append
          extra part of larger file to the end of new one
          
          ##### __TO BE DONE:__ if two files are completely different user should be prompted to
          choose if he wants to append one of them to another
