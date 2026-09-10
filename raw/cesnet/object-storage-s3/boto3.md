#

⚠️
This guide is intended for developers and advanced users. Boto3 is a Python library that can be integrated into your application.

The [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library is a Python Software Development Kit for the S3 service. It enables developers to create, configure, and manage S3 services. The library offers a simple and intuitive interface for interacting with CESNET S3 resources.

## [Installation of Boto3](#installation-of-boto3)

To use the `boto3` library, you must first install it. You can do so by running the following command in your Python environment:

```
pip install boto3

```

⚠️
**Issues with uploads in the latest boto3 versions**

Recent releases of the `boto3` library have encountered issues with third-party S3 storage providers (such as the CESNET S3 storage).

These issues are still present in versions `1.36.x` (specifically `1.36.12`). Therefore, we recommend using `boto3` version `1.35.99` or earlier.

For more details, refer to this [GitHub issue](https://github.com/boto/boto3/issues/4400).

Or you can use the specific version of the library:

```
pip install boto3==1.35.99

```

## [Usage](#usage)

First, you need to create an instance of the `s3 client` object using your credentials and the endpoint URL:

```
import boto3

access_key = "********************"
secret_key = "****************************************"
endpoint_url = "https://s3.clX.du.cesnet.cz"

s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key, endpoint_url=endpoint_url)

```

You can use the `~/.aws/credentials` file to store your credentials and use them in your scripts.
For more information, see the [official boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

You can then use the `s3` object to interact with the S3 storage. Below are several examples of how to use the Boto3 library.

**List all the buckets**

```
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(f"{bucket['Name']}")

```

**Upload an object**

```
s3.upload_file("/local/path/to/file", "bucket-name", "remote/path/to/object")

```

**Download an object** (be aware of the parameters order!)

```
s3.download_file("bucket-name", "remote/path/to/object", "/local/path/to/file")

```

**Listing the objects within bucket**

```
s3.list_objects_v2(Bucket=self.bucket)

```

or alternatively,

```
s3.list_objects(Bucket=self.bucket)

```

### On this page
[Installation of Boto3](#installation-of-boto3)[Usage](#usage)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
