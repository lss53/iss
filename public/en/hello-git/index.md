# Hello Git


A short guide to getting started with Git, without too much jargon.

<!--more-->

## Installation

- [Download Git for OSX](http://git-scm.com/download/mac)

- [Download Git for Windows](http://git-for-windows.github.io/)

- [Download Git for Linux](http://book.git-scm.com/2_installing_git.html)

## Creating a New Repository

Create a new folder, open it, then run:

```bash
git init
```

create a new git repository.

## Cloning a Repository

Run the following command to create a local clone of a repository:

```bash
git clone /path/to/repository
```

If the repository is on a remote server, your command will look something like this:

```bash
git clone username@host:/path/to/repository
```

## Workflow

Your local repository consists of three "trees" maintained by git. The first is your working directory, which holds the actual files; the second is the index (or staging area), which acts as a buffer zone temporarily holding your changes; and finally HEAD, which points to the result of your last commit.

{{< image src="trees.webp"  width="2450" height="1562" >}}

## Adding and Committing

You can stage changes (add them to the index) using the following command:

```bash
git add <filename>
git add *
```

This is the first step in the basic git workflow; use the following command to actually commit your changes:

```bash
git commit -m "commit message"
```

Now your changes are committed to HEAD, but not yet on your remote repository.

## Pushing Changes

Your changes are now in HEAD on your local repository. Run the following command to push these changes to the remote repository:

```bash
git push origin main
```

You can replace main with any branch you want to push to. If you haven't already cloned an existing repository, and want to connect your repository to a remote, you can add one using the following command:

```bash
git remote add origin <server>
```

Now you will be able to push your changes to the server you have added.

## Branching

Branches are used to isolate feature development. When you create a repository, main is the "default" branch. Develop features on other branches, and merge them into the main branch upon completion.

{{< image src="branches.webp"  width="2450" height="1562" >}}

Create a branch called "feature_x" and switch to it:

```bash
git checkout -b feature_x
```

Switch back to the main branch:

```bash
git checkout main
```

Delete the newly created branch:

```bash 
git branch -d feature_x
```

Your branch will not be visible to others unless you push it to a remote repository:

```bash
git push origin <branch>
```

## Updating and Merging

To update your local repository to the latest changes, run:

```bash 
git pull
```

to both fetch and merge changes from the remote into your working directory. To merge another branch into your current branch (e.g. main), run:

```bash
git merge <branch>
```

In both cases, git will attempt to merge the changes automatically. Unfortunately, this doesn't always work, and you may get conflicts. You will then need to edit the files and merge the conflicts manually. Once you're done, you need to mark them as successfully merged by running:

```bash
git add <filename>
```

Before merging changes, you can preview the differences using:

```bash
git diff <source_branch> <target_branch>
```

## Tagging

Creating tags for software releases is considered best practice. The concept is a relic from the past, notably used in SVN. You can create a tag called 1.0.0 by running:

```bash
git tag 1.0.0 1b2e1d63ff
```

1b2e1d63ff is the first 10 characters of the commit ID you want to tag. You can obtain the commit ID using:

```bash
git log
```

You can also use less of the commit ID prefix, as long as it points uniquely.

## Overriding Local Changes

If you've made a mistake (which of course never happens), you can override local changes using the following command:

```bash
git checkout -- <filename>
```

This will replace the file in your working directory with the latest from HEAD. Changes staged in the index, as well as new files, will not be affected. If you want to discard all your local changes and commits, and get the latest history from the server, and point your local master branch to that:

```bash
git fetch origingit reset --hard origin/master
```

#  Tips and Tricks

Built-in graphical git:

```bash 
gitk
```

Get colorful git output:

```bash
git config color.ui true
```

Only show single line entry for each commit when showing history:

```bash
git config format.pretty oneline
```

Interactively add files to the index:

```bash
git add -i
```


## Links and Resources

### Graphical Clients

- [GitX (L) (OSX, open source)](http://gitx.laullon.com/)

- [Tower (OSX)](http://www.git-tower.com/)

- [Source Tree (OSX, free)](http://www.sourcetreeapp.com/)

- [GitHub for Mac (OSX, free)](http://mac.github.com/)

- [GitBox (OSX, App Store)](https://itunes.apple.com/gb/app/gitbox/id403388357?mt=12)

### Guides and Manuals

- [Git Community Book](http://book.git-scm.com/)

- [Pro Git](http://progit.org/book/)

- [Think Like a Git](http://think-like-a-git.net/)

- [A Visual Guide to Git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)



