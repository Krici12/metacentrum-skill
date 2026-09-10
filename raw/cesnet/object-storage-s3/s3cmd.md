#

[S3cmd](https://s3tools.org/download) is a free command-line tool that enables you to upload and download data to S3 object storage. Written in Python, S3cmd is an open-source project licensed under the GNU Public License v2 (GPLv2), making it free for both personal and commercial use.

⚠️
We recommend using the AWS CLI whenever possible, as we encountered some issues with S3cmd. For example, S3cmd cannot work with buckets whose name starts with a number.

## [Installing the S3cmd Tool](#installing-the-s3cmd-tool)

S3cmd is available in the system repositories for CentOS, RHEL, and Ubuntu. You can install it using the following guide.

**On CentOS/RHEL**

```
sudo yum install s3cmd

```

**On Ubuntu/Debian**

```
sudo apt install s3cmd

```

## [Configuring the S3cmd Tool](#configuring-the-s3cmd-tool)

Add the following lines to the configuration file located at **/home/user/.s3cfg**.

```
[default]
    host_base = https://s3.clX.du.cesnet.cz
    use_https = True
    access_key = xxxxxxxxxxxxxxxxxxxxxx
    secret_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    host_bucket = s3.clX.du.cesnet.cz

```

the `host_base` and `host_bucket` refer to the S3 endpoint URL, which you received via email along with your `access_key` and `secret_key`. This information is sent to you during the S3 account creation process.

**Configuration file with GPG encryption**

```
[default]
host_base = https://s3.clX.du.cesnet.cz
    use_https = True
    access_key = xxxxxxxxxxxxxxxxxxxxxx
    secret_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    host_bucket = s3.clX.du.cesnet.cz
    gpg_command = /usr/bin/gpg
    gpg_decrypt = %(gpg_command)s -d --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
    gpg_encrypt = %(gpg_command)s -c --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
    gpg_passphrase = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

## [Basic S3cmd Commands](#basic-s3cmd-commands)

S3cmd commands support basic bucket operations - creation, listing, and deletion.

### [Bucket operations](#bucket-operations)

**Bucket name**

The bucket name must be unique within the tenant and can only contain lowercase letters, numbers, dashes, and dots. It must start with a letter or number and cannot have dots next to dashes or multiple consecutive dots.

**Listing all s3 buckets**

```
s3cmd ls

```

**Creation of a new s3 bucket**

```
s3cmd mb s3://newbucket

```

**Removing an s3 bucket**

```
s3cmd rb s3://newbucket

```

*Only emptied bucket can be removed!*

**Listing an s3 bucket size**

```
s3cmd s3://newbucket/ du

```

### [File and directory operations](#file-and-directory-operations)

**Listing of an s3 bucket**

```
s3cmd ls s3://newbucket/

```

**File upload**

```
s3cmd put file.txt s3://newbucket/

```

**Upload of encrypted files**

```
s3cmd put -e file.txt s3://newbucket/

```

**Directory upload**

```
s3cmd put -r directory s3://newbucket/

```

*Please ensure that you haven’t forgotten to remove the trailing slash (e.g. .: directory/). The trailing slash indicates that only the contents of the specified directory will be uploaded.*

**Downloading file from an s3 bucket**

```
s3cmd get s3://newbucket/file.txt

```

**Data deletion from an s3 bucket**

```
s3cmd del s3://newbucket/file.txt

s3cmd del s3://newbucket/directory

```

**Data sync to an s3 bucket from a local machine**

```
s3cmd sync /local/path/ s3://newbucket/backup/

```

**Data sync from an s3 bucket to a local machine**

```
3cmd sync s3://newbucket/backup/ ~/restore/

```

### On this page
[Installing the S3cmd Tool](#installing-the-s3cmd-tool)[Configuring the S3cmd Tool](#configuring-the-s3cmd-tool)[Basic S3cmd Commands](#basic-s3cmd-commands)[Bucket operations](#bucket-operations)[File and directory operations](#file-and-directory-operations)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
