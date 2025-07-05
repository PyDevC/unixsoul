# How to commit

we know that first we have to stage a file or a directory, but in open-source it is more than that.
Your staged file should be clear and show a clear meaning (though you can always spend hours fixing your git history)

```bash
git add <file> # only add the files which you have changed and you need to commit I don't recommend using git add . 
# If you want to stage all the files use git add -A instead
```

To commit a message You need to keep few things in mind.
Read the contribution guide for the repository first to under stand how to structure your commit

```bash
git commit -m "<message>"
# or use this instead
git commit # opens up your $EDITOR to write commit message
```
