################################################################################
# EC2 Container Service
################################################################################

# Create Cluster
resource "aws_ecs_cluster" "cluster" {
    name = "${var.ecs_cluster_name}"
}

# Create ECS service
resource "aws_ecs_service" "service" {
    depends_on = [
        "aws_autoscaling_group.ecs_asg",
        "aws_alb_target_group.ecs_targets",
        "aws_ecs_task_definition.task_def",
        "aws_iam_instance_profile.ecs_instance_profile"
    ]

    name            = "${var.class_name}"
    cluster         = "${aws_ecs_cluster.cluster.id}"
    task_definition = "${aws_ecs_task_definition.task_def.arn}"
    desired_count   = 2
    deployment_minimum_healthy_percent = 100
    deployment_maximum_percent = 200
    # Service Role for the ECS cluster
    iam_role        = "${aws_iam_role.service_role.arn}"

    # place as many containers as possible on a single EC2 instance
    # based on available memory of the instance
    placement_strategy {
      field = "memory",
      type  = "binpack"
    }

    load_balancer {
      target_group_arn = "${aws_alb_target_group.ecs_targets.arn}"
      container_name   = "${var.class_name}_container"
      container_port   = "${var.container_port}"
    }
}