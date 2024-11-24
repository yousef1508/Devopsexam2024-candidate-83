variable "region" {
  default = "eu-west-1"
}
variable "alarm_email" {
  description = "The email address to receive CloudWatch alarm notifications."
  type        = string
  default     = "yousef1508@gmail.com"
}

variable "alarm_threshold" {
  description = "The threshold for the ApproximateAgeOfOldestMessage metric, in seconds."
  type        = number
  default     = 60
  
}