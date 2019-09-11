{
    "bot": {
        "app_function": "bot.app",
        "aws_region": "us-east-1",
        "profile_name": "default",
        "project_name": "dummy-bot",
        "runtime": "python3.7",
        "s3_bucket": "$S3_BUCKET",
        "exclude": [
          "__pycache__",
          ".git/*",
          ".gitignore",
          ".python-version",
          "LICENSE",
          "README.md",
          "requirements.txt",
          "zappa_settings.json"
        ]
    }
}
