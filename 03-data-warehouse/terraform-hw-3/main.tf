terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.16.0"
    }
  }

  backend "gcs" {
    bucket = "austinmc41_tf_state_hw3"
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
