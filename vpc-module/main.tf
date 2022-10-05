resource "aws_vpc" "main" {
  cidr_block       = var.cidr
  instance_tenancy = "default"

  tags = {
    Name = "training"
  }
}

resource "aws_subnet" "public" {
  count = length(var.public_subnets)

  vpc_id     = aws_vpc.main.id
  cidr_block = element(concat(var.public_subnets, [""]), count.index)

  tags = {
    Name = "training"
  }
}

resource "aws_subnet" "private" {
  count      = length(var.private_subnets)

  vpc_id     = aws_vpc.main.id
  cidr_block = element(concat(var.private_subnets, [""]), count.index)

  tags = {
    Name = "training"
  }
}
