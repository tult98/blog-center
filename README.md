# blog-center

This is the central repository for `blog-admin` and `blog-frontend`.

## Getting started

### Download Git Repositories

Prepare an ssh key for downloading Github repository

```
ssh-keygen
cat ~/.ssh/id_rsa.pub
# copy and past the output key into Github keys settings
```

Download submodules of this central repository

```
git submodule update --init --recursive
```

Then, pull the latest code for each submodule by

```
git submodule foreach "git checkout master && git pull origin master"
```

Make `dev.py` file executable

```
chmod +x dev.py
```

Run all services

```
docker compose up -d
```

Run a specific service in interactive shell by the following command

```
./dev.py dev <service-name>
```

When there are changes to submodules. You will have to update the parent repository in case you'd like others can pulldown the latest with `git submodule update` command.

```
# in parent repository
git add <submodule_name>
git commit "Update submodule"
git push
```

**Note**: This has been done automatically by using Github action.
