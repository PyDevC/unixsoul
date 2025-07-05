# Commit format

> only add if applicable to a module or component
[modules name]: commit

> Normal commit
commit

description (write if applicable)
> NOTE: description can be omitted if the pullrequest has a detailed description
> Also the [module name]  can also be omitted if the pullrequest already has
> mentioned the module

Resolves issue: (issue id)

author: author_github_username(author github name) <email-attached to git>

## Example commit
```gitcommit
[module name]: fixed the solution for multimonitor

description:
Unixsoul hyprland seems to break for multiple monitors due to issue as described
in (# issue id), quick fix is to ... (write your solution, length of the commit depends on the pull request description)

Resolves issue: (# 123132)
author: PyDevC (Anushk Sharma) <pydevc@proton.me>

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```
