
# Example Terraform template for onboarding a new domain

variable "domain_name" {
  default = "carbon-trading"
}

resource "azurerm_storage_container" "bronze" {
  name                  = "${var.domain_name}-bronze"
  storage_account_name  = "enterpriseplatform"
  container_access_type = "private"
}

resource "azurerm_storage_container" "silver" {
  name                  = "${var.domain_name}-silver"
  storage_account_name  = "enterpriseplatform"
  container_access_type = "private"
}

resource "azurerm_storage_container" "gold" {
  name                  = "${var.domain_name}-gold"
  storage_account_name  = "enterpriseplatform"
  container_access_type = "private"
}
