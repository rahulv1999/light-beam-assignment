# light-beam-assignment
LightBeam.ai's assignment

Directory Tree is a project to replicate the folder system using data structure such as trees.

## Code base description
There are two classes Config and Folder.
The Folder class represent the folder of a system itself and behaves as a node of a tree data structure, which has child nodes which are the sub folders inside the node folder.

The Config class handels the following operations
  1. fetch by path of a folder
  2. add a sub folder to a path 
  3. remove file by its folder name
  4. update name of a folder

these operations are performed using the Folder class as its node or folder.

## Edge cases and assuptions
  1.  It is assumend that there is no cyclic relation as a root folder cannot be its own sub folder.
  2.  When removing a folder all its sub folder will also be removed
  3.  Folder name can be updated only if the folder with the new name doesn't exists
  4.  Updating a folder name with its own name should not throw error (idempotencty)
  5.  Folder update can only happen if the folder exists

main.py contains sample use of Config class

<img width="416" alt="ss" src="https://github.com/rahulv1999/light-beam-assignment/assets/48206612/c71e635c-67c2-4864-af82-e8e9c88f03ac">


output of main.py
