terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.16.0"
    }
  }

  backend "gcs" {
    bucket = "austinmc41_tf_state"
  }
}

provider "google" {
  project     = "dtc-de-course-448202"
  region      = var.region
}

resource "google_storage_bucket" "datalake_raw" {
  name          = var.raw_dtc_bucket
  location      = var.region
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "Delete"
    }
  }
}

resource "google_bigquery_dataset" "nyc_tlc_data" {
  dataset_id                  = var.tlc_bq_dataset
  location                    = var.region
  default_table_expiration_ms = 3600000
}

