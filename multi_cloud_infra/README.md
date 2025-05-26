# 🌐 Pulumi Multi-Cloud Infrastructure

This Pulumi project provisions cloud resources across **AWS**, **GCP**, and **Azure** based on user configuration.

It dynamically:
- Creates a **virtual machine**
- Provisions a **storage bucket** (S3 / GCS / Azure Blob)

---

## ✅ Features

- Works with **AWS**, **GCP**, or **Azure**
- Accepts user input via `pulumi config` for:
  - Cloud provider
  - Region
  - Machine/instance type
  - Bucket/container name
- Written in **Python**
- Easy to extend and customize

---

## 📋 Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
2. Install Python (3.7+ recommended)
3. Set up your cloud credentials:
   - **AWS**: `aws configure`
   - **GCP**: `gcloud auth application-default login`
   - **Azure**: `az login`

---

## 📁 Project Structure

multi-cloud-infra/
├── main.py # Pulumi program
├── Pulumi.yaml # Project metadata
├── README.md # You're here
└── requirements.txt # Python dependencies


---

## 📦 Installation

1. Clone the project:

```bash
git clone https://github.com/your-username/multi-cloud-infra.git
cd multi-cloud-infra

```

2. Install dependencies:
```bash
pip install -r requirements.txt

```
## ⚙️ Configuration
Set configuration values based on the provider you want to use:

```bash
pulumi config set cloud aws                # or gcp / azure
pulumi config set bucketName my-bucket
pulumi config set region us-west-1        # or us-central1 / westus2
pulumi config set machineType t2.micro    # or f1-micro / Standard_B1ls
```
## 🚀 Deploy

```bash

pulumi up

```
## 🧼 Destroy Resources
```bash
pulumi destroy

```
## ☁️ Cloud Provider Notes
🔹 AWS
EC2 instance (Amazon Linux 2)
S3 bucket

🔹 GCP
Compute Engine instance (Debian 11)
GCS bucket

🔹 Azure
Storage account + blob container
⚠️ VM setup requires additional networking configuration (not fully implemented in this version)

✅ Let us know if you'd like a full Azure VM example with VNet, NIC, and public IP setup.

## 🧪 Example Configurations
🔸 AWS
```bash
pulumi config set cloud aws
pulumi config set bucketName my-aws-bucket
pulumi config set region us-west-2
pulumi config set machineType t2.micro

```
🔸 GCP
```bash

pulumi config set cloud gcp
pulumi config set bucketName my-gcp-bucket
pulumi config set region us-central1
pulumi config set machineType f1-micro

```
🔸 Azure
```bash


pulumi config set cloud azure
pulumi config set bucketName my-azure-container
pulumi config set region westus2
pulumi config set machineType Standard_B1ls

```
## 📄 requirements.txt
The Python dependencies used in this project:

```text
pulumi>=3.0.0
pulumi-aws>=5.0.0
pulumi-gcp>=6.0.0
pulumi-azure-native>=2.0.0
```
Install them with:

```bash

pip install -r requirements.txt

```
Or generate it manually:

```bash
echo "pulumi>=3.0.0
pulumi-aws>=5.0.0
pulumi-gcp>=6.0.0
pulumi-azure-native>=2.0.0" > requirements.txt

```

## 📘 License
This project is licensed under the MIT License.

## 🙋 Need Help?
Feel free to open an issue or reach out if you'd like help extending this for:

Full Azure VM deployment

Auto-selecting machine types per region

Adding custom SSH access, firewalls, or cloud-init

Happy multi-clouding! 🌍

```