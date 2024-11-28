# Configure the Google Cloud provider
provider "google" {
  project = "<your-gcp-project-id>"
  region  = "<your-region>"
}

# Local list of files to upload
locals {
  files = [
    "file1.txt",
    "file2.sh",
    "file3.txt",
    "file4.sh",
    "file5.txt"
  ]
}

# Upload files to GCS bucket
resource "google_storage_bucket_object" "upload_files" {
  for_each = { for file in local.files : file => file }

  # Target file name: if the source file is .txt, change it to .sh
  name = each.key =~ ".txt$" ? replace(each.key, ".txt$", ".sh") : each.key

  # Bucket to upload to
  bucket = "<your-bucket-name>"

  # Source file path
  source = each.value
}