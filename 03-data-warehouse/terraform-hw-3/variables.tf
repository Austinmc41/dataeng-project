variable "region" {
    type = string
    description = "region for hosting GCP resources"
    default = "us-east1"
}

variable "raw_dtc_bucket" {
    type = string
    description = "bucket for storing NYC TLC dataset for data DTC"
    default = "austinmc41_datalake_raw_hw3"
}
