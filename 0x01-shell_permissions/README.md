
In Linux, who can do what to a file or directory is controlled through sets of permissions. There are three sets of permissions. One set for the owner of the file, another set for the members of the file’s group, and a final set for everyone else.

The permissions control the actions that can be performed on the file or directory. They either permit, or prevent, a file from being read, modified or, if it is a script or program, executed. For a directory, the permissions govern who can cd into the directory and who can create, or modify files within the directory.

You use the chmod command to set each of these permissions. To see what permissions have been set on a file or directory, we can use ls.
Viewing and Understanding File Permissions

We can use the -l (long format) option to have ls list the file permissions for files and directories.

ls -l

