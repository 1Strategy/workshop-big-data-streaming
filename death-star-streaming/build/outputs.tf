################################################################################
# OUTPUTS
################################################################################

// output "repository-name" {
//   value = "${aws_ecr_repository.test-repo.name}"
// }

// output "repository-arn" {
//   value = "${aws_ecr_repository.test-repo.arn}"
// }

// output "repository-url" {
//   value = "${aws_ecr_repository.test-repo.repository_url}"
// }

output "subnets" {
    value = "${aws_subnet.subnets.*.id}"
}

output "ecs_security_group" {
    value = "${aws_security_group.ecs.id}"
}

output "vpc_id" {
    value = "${aws_vpc.vpc.id}"
}