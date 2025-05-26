import pulumi
from pulumi import Config

# Providers
import pulumi_aws as aws
import pulumi_gcp as gcp
import pulumi_azure_native as azure

# Get user configuration
config = Config()
cloud = config.require("cloud")  # "aws", "gcp", or "azure"
bucket_name = config.require("bucketName")
region = config.require("region")
machine_type = config.require("machineType")

if cloud == "aws":
    aws_provider = aws.Provider("aws", region=region)

    bucket = aws.s3.Bucket(bucket_name,
        bucket=bucket_name,
        opts=pulumi.ResourceOptions(provider=aws_provider)
    )

    ami = aws.ec2.get_ami(
        most_recent=True,
        owners=["amazon"],
        filters=[{
            "name": "name",
            "values": ["amzn2-ami-hvm-*-x86_64-gp2"],
        }],
    )

    instance = aws.ec2.Instance("aws-instance",
        instance_type=machine_type,
        ami=ami.id,
        tags={"Name": "Pulumi-AWS-Instance"},
        opts=pulumi.ResourceOptions(provider=aws_provider)
    )

    pulumi.export("bucket_name", bucket.id)
    pulumi.export("instance_id", instance.id)

elif cloud == "gcp":
    gcp_provider = gcp.Provider("gcp", region=region)

    bucket = gcp.storage.Bucket(bucket_name,
        name=bucket_name,
        location=region,
        opts=pulumi.ResourceOptions(provider=gcp_provider)
    )

    instance = gcp.compute.Instance("gcp-instance",
        name="gcp-instance",
        machine_type=machine_type,
        zone=region + "-a",  # Adjust as needed
        boot_disk={
            "initializeParams": {
                "image": "debian-cloud/debian-11"
            }
        },
        network_interfaces=[{
            "network": "default",
            "accessConfigs": [{}]
        }],
        opts=pulumi.ResourceOptions(provider=gcp_provider)
    )

    pulumi.export("bucket_name", bucket.name)
    pulumi.export("instance_name", instance.name)

elif cloud == "azure":
    azure_provider = azure.Provider("azure", location=region)

    resource_group = azure.resources.ResourceGroup("rg",
        location=region,
        opts=pulumi.ResourceOptions(provider=azure_provider)
    )

    account = azure.storage.StorageAccount("storageacct",
        resource_group_name=resource_group.name,
        location=region,
        sku=azure.storage.SkuArgs(name=azure.storage.SkuName.STANDARD_LRS),
        kind=azure.storage.Kind.STORAGE_V2,
        opts=pulumi.ResourceOptions(provider=azure_provider)
    )

    container = azure.storage.BlobContainer(bucket_name,
        container_name=bucket_name,
        account_name=account.name,
        public_access=azure.storage.PublicAccess.NONE,
        resource_group_name=resource_group.name,
        opts=pulumi.ResourceOptions(provider=azure_provider)
    )

    # NOTE: VM provisioning in Azure requires VNet and NIC setup. This example focuses on input integration.
    pulumi.export("bucket_container", container.name)
    pulumi.export("note", "To deploy a VM in Azure, you must define network interface and OS profile setup.")

else:
    raise Exception("Unsupported cloud provider. Use 'aws', 'gcp', or 'azure'.")