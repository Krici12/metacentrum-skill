#

Accessing the storages directly is not as straightforward as accessing the frontends. Due to operational reasons only a selection of commands is allowed.

This chapter will give you some insight into direct data manipulation on storages.

## [ssh protocol](#ssh-protocol)

Selected commands for data manipulation directly at the storage server can be run through `ssh`.

💡
Tip

When copying files with `dd` set block size (bs parameter) to at least 1 M. Operations will be faster.

Apart from the **cerit storages** (those with “cerit” in the name of the server), there is **no shell** available on storage servers, so `ssh user123@storage_name.metacentrum.cz` will not work. Instead, use the construction like `ssh user123@storage_name.metacentrum.cz command`.

On storage servers, only the following commands are available:

```
cat
chmod
cp
dd
du
getfacl
gunzip
gzip
ls
mkdir
mv
ncdu2
rm
rmdir
rsync
s3cmd
s5cmd
scp
setfacl
ssh
tar

```

No ssh by login and password to storage-du-cesnet.metacentrum.cz

Since April 2023, CESNET Storage department service does not allow to log in to their servers by login and password. To `ssh` to `storage-du-cesnet.metacentrum.cz`, users have to use either Kerberos ticket or ssh keys. See more on [Cesnet Storage Department service pages](https://du.cesnet.cz/en/novinky/start).

**Example**

List the content of home directory on remote machine:

```
ssh USERNAME@storage-brno6.metacentrum.cz ls -l

```

or

```
ssh USERNAME@storage-brno6.metacentrum.cz ls -l /home/USERNAME

```

## [Mount storages locally](#mount-storages-locally)

For more advanced users, there is also the possibility to mount the data storages locally. The NFS4 servers can then be accessed in the same way as local disk.

For more detail, follow the tutorial on [how to mount storages on local station](../computing/infrastructure/mount-storages).

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[ssh protocol](#ssh-protocol)[Mount storages locally](#mount-storages-locally)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
