#

This is for Linux and macOS

This page contains a tutorial on how to mount storage locally on Linux and macOS machines. There is no free client for MS-Windows, only the commercial NFS Maestro.

**List of current storage servers**

## [Storage information](#storage-information)

| Server |Directory |Backup Class |Note |
| storage-brno2.metacentrum.cz |/storage/brno2/ |2 | |
| storage-brno11-elixir.metacentrum.cz |/storage/brno11-elixir/ |2 |dedicated to ELIXIR-CZ |
| storage-brno12-cerit.metacentrum.cz |/storage/brno12-cerit/ |2 | |
| storage-plzen1.metacentrum.cz |/storage/plzen1/ |2 | |
| storage-plzen2-zcu.metacentrum.cz |/storage/plzen2-zcu/ |3 |dedicated to ZČU groups |
| storage-plzen4-ntis.metacentrum.cz |/storage/plzen4-ntis/ |3 |dedicated to iti/kky groups |
| storage-praha2-natur.metacentrum.cz |/storage/praha2-natur/ |0 | |
| storage-praha6-fzu.metacentrum.cz |/storage/praha6-fzu/ |0 | |
| storage-praha5-elixir.metacentrum.cz |/storage/praha5-elixir/ |3 | |
| storage-budejovice1.metacentrum.cz |/storage/budejovice1/ |3 | |
| storage-liberec3-tul.metacentrum.cz |/storage/liberec3-tul/ |0 | |
| storage-pruhonice1-ibot.metacentrum.cz |/storage/pruhonice1-ibot/ |3 | |
| storage-vestec1-elixir.metacentrum.cz |/storage/vestec1-elixir/ |2 |also /storage/praha1/ |

## [Backup class description](#backup-class-description)

| Backup Class |Description |
| 0 |No backup. |
| 2 |Snapshot backups once a day. Backups are performed and stored on the same HW as primary data. This class provides protection against unintentional data removal. It does not protect against hardware failure of the storage. |
| 3 |Snapshot backups plus a backup copy. The copy resides on a different hardware. This class provides protection against unintentional data removal as well as hardware failures. |

## [Connection setup](#connection-setup)

You will need to do several things to make NFSv4 accessible on your Linux desktop:

Administrator access is required

You must have root privileges on your local PC.

### [Create mount points](#create-mount-points)

You need to create an empty directory where the Metacentrum NFS volumes will be mounted. We recommend the directory `/storage` because this is what is set on MetaCentrum machines. E.g.:

```
mkdir /storage
mkdir /storage/brno12-cerit
mkdir /storage/brno2
mkdir /storage/plzen1
...

```

You can choose an arbitrary name and location for the mounting points - just remember to modify the steps described below.

### [Install Kerberos support](#install-kerberos-support)

If your PC does not have Kerberos system support enabled, you need to install it first. On Debian-based systems, you can do:

```
apt install krb5-user

```

Once Kerberos support is installed, you must provide proper configuration in `/etc/krb5.conf`. The easiest way is to copy it simply from a MetaCentrum machine, e.g skirit.ics.muni.cz, e.g. :

```
scp user@skirit.ics.muni.cz:/etc/krb5.conf /etc/

```

Verify that Kerberos is correctly enabled

```
kinit user@META
klist

```

### [Get Kerberos credentials for your NFS](#get-kerberos-credentials-for-your-nfs)

The following command replaces an existing krb5.keytab! If you already have one, you need to update its content using ‘ktutil’ command.

```
$ ssh user@skirit.metacentrum.cz '/software/remctl-2.12/bin/remctl -d kdccesnet.ics.muni.cz accounts nfskeytab' > /etc/krb5.keytab

```

Set its ownership to root:root and rights to 600 as follows:

```
chown root:root /etc/krb5.keytab
chmod 600 /etc/krb5.keytab

```

### [Install client NFSv4 tools](#install-client-nfsv4-tools)

On Debian-base system:

```
apt-get install nfs-common

```

You will also need a running portmap. It should be installed with nfs-utils dependencies. Otherwise, install the package portmap separately.

**nfs-utils setting on Debian/Ubuntu**

Setting of nfs-utils is in the file `/etc/default/nfs-common`. Set the values in the following way:

```
NEED_STATD=yes
STATDOPTS=
NEED_IDMAPD=yes
NEED_GSSD=yes

```

**nfs-utils setting on OpenSUSE**

Setting of nfs-utils in the file `/etc/sysconfig/nfs`. Set at least the following values:

```
NFS_SECURITY_GSS="yes"
NFS4_SUPPORT="yes"

```

### [Enable automatic mount on boot](#enable-automatic-mount-on-boot)

For storage you wish to mount locally, add the following lines to the `/etc/fstab` file:

```
storage-brno12-cerit.metacentrum.cz:/ /storage/brno12-cerit  nfs4       sec=krb5i             0 0
storage-plzen1.metacentrum.cz:/ /storage/plzen1           nfs4       sec=krb5i             0 0
...

```

Note

Due to hardware replacement, the data are moved continuously from one storage to another. For backwards compatibility, the old names of storages (e.g. brno2) are kept as symbolic links. The target in `/etc/fstab` must be a real directory, not a symlink. By using `ls -l`, you can find where the symbolic links lead.

Sample of `/etc/fstab`:

```
storage-brno12-cerit.metacentrum.cz:/ /storage/brno12-cerit  nfs4 sec=krb5i       0 0
storage-brno2.metacentrum.cz:/ /storage/brno2  nfs4 sec=krb5i       0 0
storage-liberec3-tul.metacentrum.cz /storage/liberec3-tul nfs4 sec=krb5i       0 0
...

```

Note

Due to privacy reasons, some repositories can be accessed only from Metacentrum IP addresses. Storages of the form CITY+NUMBER, like brno2 or praha1 should always be mountable. Usually, the “private” repositories with limited access are the ones with a suffix in their name (-kky, -fzu, etc.).

For example, if you get an error like

```
mount.nfs4: access denied by server while mounting storage-plzen3-kky.metacentrum.cz:/

```

This is very likely the case. Simply delete the line from `/etc/fstab` if you can’t mount it from your location.

### [Start nfs client and remount all volumes](#start-nfs-client-and-remount-all-volumes)

You don’t need to mount a volume in OpenSuse 11.1, because running nfs service connects it automatically according to the records in `/etc/fstab`, in other OS, explicit mounting (`mount -a`) is needed.

Now the Metacentrum NFSv4 volumes should be mounted to mount points specified in `/etc/fstab` file.

### [Accessing user data on NFS4 storage](#accessing-user-data-on-nfs4-storage)

To be able to access your user data, you must have a valid kerberos ticket. You can obtain one by calling the `kinit` command:

```
kinit user@META

```

Verify you can access your home directly:

```
ls /storage/brno2/home/user123

```

## [Concluding notes](#concluding-notes)

### [Simple settings of idmapd.conf](#simple-settings-of-idmapdconf)

File `/etc/idmapd.conf` sets mapping of NFSv4 identities to local users (NFSv4 works with text principals of Kerberos, the POSIX interface of the file system works with numerical representation of users and groups).

A simple configuration of `/etc/idmapd.conf` can look the following way: `Domain = META`. Users from the domain @META will be mapped through to files `/etc/passwd` and `/etc/group`. This means that for the identity `user_123@META` there must exist a record in `/etc/passwd` with the name `user\_123`. Ordinary tools (`ls -l`) will show the names properly if the name in the given files exists for their principal. For nonexisting name user will be mapped as nobody and nogroup.

Example:

```
grep user_123 /etc/passwd
user_123:x:1000:1000:User 123       ,,,:/home/user_123:/bin/bash
ls -l /mnt/nfs/software
total 0
drwxr-xr-x 4 nobody   nogroup   51 2008-06-12 12:49 etics
-rw-r--r-- 1 nobody   nogroup    0 2008-06-06 14:26 hu
drwxr-xr-x 6 user_123 soft-nfs4 54 2008-06-12 14:45 libnfsidmap
drwxr-xr-x 5 user_123 soft-nfs4 40 2008-06-11 13:12 nsswitch

```

Since both a record for user `user\_123@META` exists in `/etc/passwd` and a record for group soft-nfs4@META exists in `/etc/group`, the mapping is created and displayed. There is no record for the user who owns directory `etics`, that is why it’s shown as `nobody:nogroup`.

### [Proper displaying of users and groups names](#proper-displaying-of-users-and-groups-names)

Above-mentioned settings of idmapd.conf will be displayed properly only if users and groups are stored in `/etc/passwd` and `/etc/group`. Moreover, the user or group must be from the META domain. Cross-realm user mappings are possible through advanced settings. It is necessary to set the mapping of NFSv4 identities to numerical representation and to set a mapping of numerical representations to individual names.

### [Cross-realm mapping NFSv4 identities to numerical representation](#cross-realm-mapping-nfsv4-identities-to-numerical-representation)

It is necessary to reach mapping files of users and groups for mapping support.

- [http://meta.cesnet.cz/nfs4/passwd-nfs4](http://meta.cesnet.cz/nfs4/passwd-nfs4)

- [http://meta.cesnet.cz/nfs4/group-nfs4](http://meta.cesnet.cz/nfs4/group-nfs4)

You have to save these files to `/etc/passwd-nfs4` and `/etc/group-nfs4`.

Ensure you have installed the latest version of the `libnfsidmap` library. The installation files are located in `/storage/software/libnfsidmap`, which contains binaries for IA32 and X86_64 architectures (within the lib32 and lib64 directories, respectively), as well as Debian packages for i386 and AMD64.

To implement this advanced mapping, first ensure the basic configuration described above is functional. Once you have obtained the necessary packages and mapping files, update your `idmapd.conf` settings to enable the new configuration.

```
[Translation]
Method = mnsswitch

```

The existing configuration may be similar. However, new settings must use `mnsswitch` instead of `nsswitch`. We keep the settings `Domain = META` the same.

Restart service idmapd:

```
Debian: systemctl restart nfs-idmapd,

```

Now we have cross realm mapping of NFSv4 identities to numerical representation for POSIX interface.

### [Cross-realm mapping of numerical representation to names](#cross-realm-mapping-of-numerical-representation-to-names)

Nsswitch handles the translations across-realms.

Download the `libnss-nfs4.so.2` library from the NFS share at `/storage/software/nsswitch` and place it in the `/lib` directory. Debian versions for both i386 and X86_64 architectures are available. No separate installation package is provided, as the library consists of this single file.

Change the configuration of `/etc/nsswitch.conf` in the following way:

```
passwd:         compat nfs4
group:          compat nfs4

```

Add nfs4 to the end of the `passwd` and `group` lines.

You don’t have to restart the service; the new mapping should work immediately.

Names with domains are written implicitly. If we don’t want to write some domain again and again, it is possible to export the environment variable NFS4DOMAIN=META.

```
export NFS4DOMAIN=META

```

then names from the domain META will be shown without this domain in the list.

### [Set up/check NFSv4 support in kernel](#set-upcheck-nfsv4-support-in-kernel)

If you are using Ubuntu or OpenSUSE kernel, you can skip this step, as they already have NFS4 enabled. Otherwise, ensure the support in the following way:

**Test of support for the NFS file system**

```
grep nfs4 /proc/filesystems

```

You should get: `nodev nfs4`.

In case of an empty answer, run as root:

```
$ modprobe nfs

```

and repeat the test. In case of a negative answer, it is necessary to compile NFS (with NFSv4 support) into the kernel.

**Test RPCSECsupport**

```
ls -d /proc/net/rpc/auth.rpcsec*

```

The output should look like this: `proc/net/rpc/auth.rpcsec.context /proc/net/rpc/auth.rpcsec.init`

If it looks like this: `ls: cannot access /proc/net/rpc/auth.rpcsec*: No such file or directory`, run as a root

```
modprobe auth_rpcgss

```

and repeat the test. If the response is still negative, it is necessary to compile `CONFIG_SUNRPC_GSS` into the Linux kernel.

**Automatic insertion of modules**

If the system supports NFSv4 with RPCSEC, it is not necessary to insert modules manually - client tools insert NFS on their own.

### [Installation for Gentoo](#installation-for-gentoo)

You need to install packages `net-nds/rpc-bind` and `net-fs/nfs-utils`. Check whether nfs-utils are compiled with kerberos.

Scripts for a start nfs in Gentoo are little bit odd because they have common settings of server and client. Settings of nfs-utils is in the file `/etc/conf.d/nfs` where you need to change “OPTS_RPC_GSSD” to the value ” — -n ” in case you use your own key and not the machine keytab.

Next, ensure modules `nfs` and `rpcsec_gss_krb5` are downloaded and set them to load after booting the system. The scripts can’t load them themselves.

Configure `/etc/idmapd.conf`, as is described above, simply rewrite Domain to META in the pattern file and return to this place in the tutorial.

You need to run services rpc-gssd and rpc-idmapd, on systemd run: `systemctl enable --now rpc-gssd nfs-idmapd`

Add the following line into `/etc/fstab`

```
storage-brno2.metacentrum.cz:/ /storage nfs4 sec=krb5i

```

and run `systemctl daemon-reload; systemctl restart remote-fs.target`. Volume should mount now.

### [Installation for macOS](#installation-for-macos)

Users must be able to obtain the Kerberos ticket on their local machine. Follow this tutorial on how to get a krb5 ticket.

Once `kinit` command successfully generates valid krb5 tickets, add the line `nfs.client.default_nfs4domain = META` to the end of the file `/etc/nfs.conf` as superuser.

You have to create an empty directory where the Metacentrum storage NFS volume will be mounted. For example:

```
mkdir /path/on/my/local/computer/storage-praha5-elixir

```

Finally, you can mount the selected NFS volume (as superuser).

```
mount_nfs -o vers=4,sec=krb5i storage-praha5-elixir.metacentrum.cz:home/your_username /path/on/my/local/computer/storage-praha5-elixir

```

The example above will mount your home directory on the storage praha5-elixir to the specified directory on the local computer.

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[Storage information](#storage-information)[Backup class description](#backup-class-description)[Connection setup](#connection-setup)[Create mount points](#create-mount-points)[Install Kerberos support](#install-kerberos-support)[Get Kerberos credentials for your NFS](#get-kerberos-credentials-for-your-nfs)[Install client NFSv4 tools](#install-client-nfsv4-tools)[Enable automatic mount on boot](#enable-automatic-mount-on-boot)[Start nfs client and remount all volumes](#start-nfs-client-and-remount-all-volumes)[Accessing user data on NFS4 storage](#accessing-user-data-on-nfs4-storage)[Concluding notes](#concluding-notes)[Simple settings of idmapd.conf](#simple-settings-of-idmapdconf)[Proper displaying of users and groups names](#proper-displaying-of-users-and-groups-names)[Cross-realm mapping NFSv4 identities to numerical representation](#cross-realm-mapping-nfsv4-identities-to-numerical-representation)[Cross-realm mapping of numerical representation to names](#cross-realm-mapping-of-numerical-representation-to-names)[Set up/check NFSv4 support in kernel](#set-upcheck-nfsv4-support-in-kernel)[Installation for Gentoo](#installation-for-gentoo)[Installation for macOS](#installation-for-macos)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
