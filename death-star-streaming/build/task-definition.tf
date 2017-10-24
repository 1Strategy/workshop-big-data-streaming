################################################################################
# Task Definition
################################################################################

resource "aws_ecs_task_definition" "task_def" {
    family                = "${var.class_name}_task"
    container_definitions = <<DEFINITION
[
  {
    "cpu": 0,
    "essential": true,
    "image": "${var.docker_image}",
    "memory": ${var.container_memory},
    "name": "${var.class_name}_container",
    "portMappings": [
      {
        "containerPort": ${var.container_port}
      }
    ],
    "environment": [
      {
        "name": "AWS_REGION",
        "value": "${var.aws_region}"
      },
      {
          "name": "STREAM_NAME",
          "value": "TesterBot"
      }
    ]
  }
]
DEFINITION
}