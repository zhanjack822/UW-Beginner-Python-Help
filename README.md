# UW-2022-First-Year-Physics-Coding
A repository where first year students can submit code snippets and receive feedback from their upper classmen.

# Instructions on setting up a local repository

1. The first thing you need to do is clone the repository. To do this, open a terminal (in administrator mode in Windows) and navigate to the directory where you want the repository folder to be cloned to. It's recommended that this note be in your user directory, which contains your commonly used directories for your desktop, downloads, documents, etc. If you haven't used a terminal before, simply copy the address of the desired directory and use:
    ```console
    cd PATH/TO/DIRECTORY
    ```
    If your directory path includes spaces, enclose the path with quotation marks. Once you have navigated to this directory in your terminal, enter the following command:
    ```console
    git clone https://github.com/zhanjack822/UW-2022-First-Year-Physics-Coding.git
    ```
    The cloned repository on your computer is referred to as a "local repository" while the repository on GitHub is referred to as the "remote repository."
    
2. Create a branch from the master branch with your name as the branch name.
    ```console
    git checkout master
    ```
    ```console
    git checkout -b YOUR_NAME
    ```
    Note that `checkout` without the `-b` flag is used to switch between branches.

3. In the home directory of your local repository, create a folder to store your code. You can do this using the desktop GUI or in a terminal using `mkdir YOUR_NAME` or the equivalent of `mkdir` on your operating system.

4. Now that you've made your first change, it's helpful to know how to commit changes to the remote repository. First, check what has been changed on your local repository since your last commit by using:
    ```console
    git status
    ```
    
5. Any changes that haven't been added to the next commit will appear in red, usually with a note on what command needs to be run to add these changes.
    * For files that have been added, use:
        ```console
        git add FILE_NAME
        ```
    * For directories (i.e. folders) that have been added, use:
        ```console
        git add DIRECTORY_NAME/
        ```
        Note that your directory will only be tracked if it isn't empty. Add a README.md file with a basic description (e.g. "My code") so that you can the directory. Note that you should only add the directory with the README.md file initially, before you've added any other content. This is explained in step 8. Add the directory first, commit it, and then add any files you want to include in that directory and commit those as well.
    * For files that have been removed, use:
        ```console
        git rm FILE_NAME
        ```
    * For directories that have been removed, use:
        ```console
        git rm -r DIRECTORY_NAME
        ```
        Note that this will also remove all files within the directory as well. While it is bad form to add all the files in a directory at once, this doesn't hold true for removing directories that contain files.
        
6. Now commit changes you've made using:
    ```console
    git commit -m "Your commit message."
    ```
    Your commit message should briefly explain the changes that were made. Because every file modified or added should have its own commit message, you should add each file and commit it separately. This allows tracking of changes easier for those keeping tabs on the repository.
    
7. After the changes have all been committed, push them to the remote repository. For your first push after creating a new branch, use:
    ```console
    git push -u origin NAME_OF_YOUR_BRANCH
    ```
    Every subsequent push can be made with the simplified command:
    ```console
    git push
    ```
8. If a change has been made to the remote repository that you want included on your local repository, use:
    ```console
    git pull
    ```
    
9. Lastly, to merge your branch with the master branch, create a pull request. Title your pull request and add a description that explains what has been modified and what you would like people to look over. Add someone as your reviewer and make the pull request. The reviewer will look over your code and makes comments inquiring about your code or making helpful suggestions. If the reviewer requires a change be made, make the required change on your local repository and push the changes. The pull request will always switch to the most up-to-date commit of your branch. When the reviewer is satisfied, they will approve the change. You may have compatability issues between your branch and the master branch. If that is the case, GitHub has the ability to open the files with conflicts and you can make your changes there. Alternatively, your local repository files will be edited to show where the conflicts are, and using an editor, particularly one with git compatability (e.g. PyCharm, VSCode, VS), you can resolve the conflicts on your local repo and push the changes; this is the preferred method. Once all conflicts are resolved, you can merge your branch with the master branch.
    
# Discussions

In the discussions tab at the top of the webpage, you can create a discussion to inquire about some specific topic or ask questions about code in one of the branches.
