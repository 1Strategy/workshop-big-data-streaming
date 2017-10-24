################################################################################
# AutoScaling Group
################################################################################

resource "aws_autoscaling_group" "ecs_asg" {
    depends_on = [
        "aws_launch_configuration.launch_config",
        "aws_subnet.subnets"
    ]

    name                      = "${var.class_name}_asg"
    availability_zones        = ["${var.azs}"]
    max_size                  = "${var.asg_max}"
    min_size                  = "${var.asg_min}"
    desired_capacity          = "${var.asg_desired}"
    health_check_type         = "EC2"
    health_check_grace_period = 300
    force_delete              = true
    launch_configuration      = "${aws_launch_configuration.launch_config.name}"
    vpc_zone_identifier       = ["${aws_subnet.subnets.*.id}"]

    tag {
        key                 = "Built By"
        value               = "${var.class_name} Autoscaling Group"
        key                 = "Name"
        value               = "${var.class_name} Instance"
        propagate_at_launch = true
    }
}